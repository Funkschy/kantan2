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
            'name': 'first',
            'instances': ['def first() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'i',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'j',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'k',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
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
                                'value': 'i',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'assign',
                                'ty': 'i32',
                                'left': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'j',
                                },
                                'op': '=',
                                'right': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'k',
                                }
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
                                'value': 'i',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 1
                            }
                        }
                    }
                ]
            }
        },
        {
            'kind': 'func_def',
            'name': 'second',
            'instances': ['def second() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'i',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'j',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'k',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
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
                                'value': 'i',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'assign',
                                'ty': 'i32',
                                'left': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'j',
                                },
                                'op': '=',
                                'right': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'k',
                                }
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
                                'value': 'j',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 1
                            }
                        }
                    }
                ]
            }
        },
        {
            'kind': 'func_def',
            'name': 'third',
            'instances': ['def third() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'i',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'j',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'k',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': 'i32',
                            'value': 'undefined'
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
                                'value': 'i',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'assign',
                                'ty': 'i32',
                                'left': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'j',
                                },
                                'op': '=',
                                'right': {
                                    'kind': 'identifier',
                                    'ty': 'i32',
                                    'value': 'k',
                                }
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
                                'value': 'k',
                                'ty': 'i32'
                            },
                            'op': '=',
                            'right': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 1
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
