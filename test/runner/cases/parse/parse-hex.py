from pathlib import Path
from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got

expected_modules = [{
    'kind': 'module',
    'path': str(Path(__file__).parent) + '/parse-hex.kan',
    'items': [
        {
            'kind': 'func_def',
            "name": "main",
            "ret": "void",
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'value': 0xa101b3f
                        }
                    }
                ]
            }
        }
    ]
}]


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options.append('--dump-ast')

    def test_output(self, output: Output) -> Optional[TestError]:
        super_error = super().test_output(output)
        if super_error is not None:
            return super_error

        modules = output.modules
        if modules != expected_modules:
            return expected_but_got('modules', expected_modules, modules)
