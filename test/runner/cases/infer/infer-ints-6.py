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
            'instances': ['() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'test',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'p',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': '*i32',
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'p2',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': '*i32',
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': '*i32',
                            'left': {
                                'kind': 'identifier',
                                'ty': '*i32',
                                'value': 'p2',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': '*i32',
                                'value': 'p',
                            }
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': 'i32',
                            'left': {
                                'kind': 'unary',
                                'ty': 'i32',
                                'op': '*',
                                'right': {
                                    'kind': 'identifier',
                                    'ty': '*i32',
                                    'value': 'p',
                                }
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': 'i32',
                                'value': 'test',
                            }
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': 'i32',
                            'left': {
                                'kind': 'identifier',
                                'ty': 'i32',
                                'value': 'test',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 0,
                            }
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': '*i32',
                            'value': 'p'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': '*i32',
                            'value': 'p2'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': 'i32',
                            'value': 'test'
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
