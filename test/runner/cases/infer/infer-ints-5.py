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
            'name': 'main',
            'instances': ['def main() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'i',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'u32',
                            'value': 0
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'u',
                        'ty': 'u32',
                        'value': {
                            'kind': 'literal',
                            'ty': 'u32',
                            'value': 0
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'p',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': '*u32',
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': 'u32',
                            'left': {
                                'kind': 'unary',
                                'ty': 'u32',
                                'op': '*',
                                'right': {
                                    'kind': 'identifier',
                                    'ty': '*u32',
                                    'value': 'p',
                                }
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': 'u32',
                                'value': 'i',
                            }
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': 'u32',
                            'left': {
                                'kind': 'identifier',
                                'ty': 'u32',
                                'value': 'u',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': 'u32',
                                'value': 'i',
                            }
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': '*u32',
                            'value': 'p',
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': 'u32',
                            'value': 'i',
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': 'u32',
                            'value': 'u',
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
