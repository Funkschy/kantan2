import sys
from os.path import splitext
from pathlib import Path
from typing import Optional, List, Union

from runner.execute import CompilerExecutor
from runner.output import Output, OutputElement


class TestError(object):
    def __init__(self, msg: str):
        self.msg = msg


def base_filename(file) -> str:
    return splitext(file)[0]


def relative_to_base(file, relative) -> str:
    return str(Path(base_filename(file)).parent.joinpath(Path(relative)).resolve())


def kantan_filename(file) -> str:
    return base_filename(file) + '.kan'


class TestCase(object):
    def __init__(self, executor: CompilerExecutor, options=None):
        if options is None:
            options = ['--mi']
        self.options = options
        self.executor = executor

    def base_filename(self) -> str:
        return base_filename(sys.modules[self.__module__].__file__)

    def kantan_filename(self) -> str:
        return self.base_filename() + '.kan'

    def files(self) -> List[str]:
        return [self.kantan_filename()]

    def run(self) -> Union[Output, List[str]]:
        return self.executor.run(self.base_filename(), self.files(), self.options)

    def test_output(self, output: Output) -> Optional[TestError]:
        raise RuntimeError('You forgot to override run')


class SuccessTestCase(TestCase):
    def __init__(self, executor: CompilerExecutor, options=None):
        super().__init__(executor, options)

    def test_output(self, output: Output) -> Optional[TestError]:
        if output.rc != 0:
            return TestError(f'expected 0 as return code, but got {output.rc}')

        if len(output.errors) > 0:
            return TestError(f'expected 0 errors, but got {len(output.errors)}')

        return None


class ErrorTestCase(TestCase):
    def __init__(self, executor: CompilerExecutor, expected_errors, options=None):
        super().__init__(executor, options)
        self.expected_errors = expected_errors

    def simple_error(self, lnr: int, col: int, msg: str, file: Optional[str] = None) -> OutputElement:
        return self.simple_element("error", lnr, col, msg, file)

    def note_error(self, lnr: int, col: int, msg: str, notes: List[OutputElement],
                   file: Optional[str] = None) -> OutputElement:
        if file is None:
            file = self.kantan_filename()
        return OutputElement('error', lnr, col, str(msg), file, notes)

    def simple_note(self, msg: str):
        return self.simple_element('note', 0, 0, msg, '')

    def simple_element(self, ty: str, lnr: int, col: int, msg: str, file: Optional[str] = None) -> OutputElement:
        if file is None:
            file = self.kantan_filename()
        return OutputElement(ty, lnr, col, str(msg), file, [])

    def test_output(self, output: Output) -> Optional[TestError]:
        if len(output.errors) != len(self.expected_errors):
            return expected_but_got('number of errors', len(self.expected_errors), len(output.errors))

        for i in range(len(output.errors)):
            expected = self.expected_errors[i]
            actual = output.errors[i]

            error = test_element(expected, actual)
            if error is not None:
                return error

            if len(actual.notes) == 0:
                continue

            if len(actual.notes) != len(expected.notes):
                return expected_but_got('number of notes', len(expected.notes), len(actual.notes))

            for j in range(len(actual.notes)):
                expected_note = expected.notes[j]
                actual_note = actual.notes[j]

                error = test_element(expected_note, actual_note)
                if error is not None:
                    return error

        return None


def expected_but_got(name: str, expected, actual) -> TestError:
    return TestError(f'wrong {name}, expected "{expected}", but got "{actual}"')


def test_element(expected: OutputElement, actual: OutputElement) -> Optional[TestError]:
    if expected.type != actual.type:
        return expected_but_got('type', expected.type, actual.type)

    if expected.lnr != actual.lnr:
        return expected_but_got('lnr', expected.lnr, actual.lnr)

    if expected.col != actual.col:
        return expected_but_got('col', expected.col, actual.col)

    if expected.content != actual.content:
        return expected_but_got('content', expected.content, actual.content)

    if expected.file != actual.file:
        return expected_but_got('file', expected.file, actual.file)

    return None
