from pathlib import Path
from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got

expected_modules = [{
    'kind': 'module',
    'path': str(Path(__file__).parent) + '/parse-simple-expr2.kan',
    'imports': [],
    'items': [
        {
            'kind': 'func_def',
            'name': 'main',
            'instances': ['(i32, **i8) -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'binary',
                            'ty': 'i32',
                            'left': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 1
                            },
                            'op': '+',
                            'right': {
                                'kind': 'binary',
                                'ty': 'i32',
                                'left': {
                                    'kind': 'literal',
                                    'ty': 'i32',
                                    'value': 2
                                },
                                'op': '*',
                                'right': {
                                    'kind': 'literal',
                                    'ty': 'i32',
                                    'value': 3
                                }
                            }
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
