from pathlib import Path
from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got

expected_modules = [{
    'kind': 'module',
    'path': str(Path(__file__).parent) + '/parse-literals.kan',
    'imports': [],
    'items': [
        {
            'kind': 'func_def',
            "name": "main",
            "instances": [],  # this file is only parsed, not type checked
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 'test'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 'a'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 45054
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 1
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'literal',
                            'ty': None,
                            'value': 3.14
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
        # otherwise we'll get some annoying type errors
        self.options.append('--parse-only')

    def test_output(self, output: Output) -> Optional[TestError]:
        super_error = super().test_output(output)
        if super_error is not None:
            return super_error

        modules = output.modules
        if modules != expected_modules:
            return expected_but_got('modules', expected_modules, modules)
