from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    'kind': 'module',
    'path': kantan_filename(__file__),
    'imports': [],
    'items': [
        {
            'kind': 'func_def',
            'name': 'f',
            'instances': ['def f(*i8, isize) -> void'],
            'body': {
                'kind': 'block',
                'stmts': []
            }
        },
        {
            'kind': 'func_def',
            'name': 'main',
            'instances': ['def main() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 's',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': '*i8',
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'len',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'isize',
                            'value': 0
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def f(*i8, isize) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'identifier',
                                    'ty': '*i8',
                                    'value': 's',
                                },
                                {
                                    'kind': 'identifier',
                                    'ty': 'isize',
                                    'value': 'len',
                                }
                            ]
                        }
                    },
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
