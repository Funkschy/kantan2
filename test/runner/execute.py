import os
import subprocess
from pathlib import Path
from typing import List, Optional, Union

from runner.output import Output, parse_output

error_rc = 255
segfault_rc = -11
abort_rc = -6


def valgrind(filename: str, suppress_path: Optional[str]) -> List[str]:
    cmd = ['valgrind']

    if suppress_path is not None:
        cmd += [f'--suppressions={suppress_path}']

    return cmd + [
        '--leak-check=full',
        '--error-exitcode=' + str(error_rc),
        '--xml=yes',
        '--xml-file={}.xml'.format(filename)
    ]


class ValgrindOptions(object):
    def __init__(self, use_valgrind: bool, suppress_file: str):
        self.use_valgrind = use_valgrind
        self.suppress_file = suppress_file


class ExecutionError(object):
    def __init__(self, msg: str, raw: str):
        self.msg = msg
        self.raw = raw


# actually runs the compiler
class CompilerExecutor(object):
    def __init__(self, compiler_path: str, valgrind_opts: ValgrindOptions):
        self.compiler_path = compiler_path
        self.valgrind_opts = valgrind_opts

    def _run(self, filename: str, files: List[str], options: List[str]):
        cmd = [self.compiler_path] + options + files
        if self.valgrind_opts.use_valgrind:
            cmd = valgrind(filename, self.valgrind_opts.suppress_file) + cmd

        completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Path.cwd())

        # the output could just be a string, if the NonParsingExecutor was used
        if self.valgrind_opts.use_valgrind:
            raw_stdout = completed_process.stdout.decode('utf-8')
            # check for valgrind errors
            if completed_process.returncode == error_rc:
                return ExecutionError(f'{filename} has memory leaks', raw_stdout)
            if completed_process.returncode == segfault_rc:
                return ExecutionError(f'{filename} has crashed', raw_stdout)
            if completed_process.returncode == abort_rc:
                return ExecutionError(f'{filename} has aborted', raw_stdout)

            # cleanup useless valgrind xml files, only keep them for failed tests
            os.remove(filename + '.xml')

        return completed_process

    def run(self, filename: str, files: List[str], options: List[str]) -> Union[Output, ExecutionError]:
        completed_process = self._run(filename, files, options)
        if type(completed_process) is ExecutionError:
            return completed_process

        parsed = parse_output(completed_process)
        if type(parsed) is Output:
            return parsed

        raw_stdout = completed_process.stdout.decode('utf-8')
        return ExecutionError(' '.join(parsed), raw_stdout)


class PredicateCompilerExecutor(CompilerExecutor):
    def __init__(self, base: CompilerExecutor, predicates):
        super().__init__(base.compiler_path, base.valgrind_opts)
        self.predicates = predicates

    def run(self, filename: str, files: List[str], options: List[str]) -> Optional[Output]:
        for predicate in self.predicates:
            if not predicate():
                return None

        return super().run(filename, files, options)


class NonParsingExecutor(CompilerExecutor):
    def __init__(self, base: CompilerExecutor):
        super().__init__(base.compiler_path, base.valgrind_opts)

    def run(self, filename: str, files: List[str], options: List[str]) -> Optional[str]:
        completed_process = self._run(filename, files, options)
        if type(completed_process) is ExecutionError:
            return completed_process

        return completed_process.stdout.decode('utf-8')
