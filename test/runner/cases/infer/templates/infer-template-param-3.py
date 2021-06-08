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
            'instances': [
                'def f(*i32) -> void',
                'def f(*i8) -> void'
            ],
            'body': {
                'kind': 'block',
                'stmts': []
            }
        },
        {
            'kind': 'func_def',
            'name': 'main',
            'instances': [
                'def main() -> void'
            ],
            'body': {
                'kind': 'block',
                'stmts': [

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
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def f(*i32) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'identifier',
                                    'ty': '*i32',
                                    'value': 'p',
                                }
                            ]
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'p2',
                        'ty': None,
                        'value': {
                            'kind': 'literal',
                            'ty': '*i8',
                            'value': 'undefined'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def f(*i8) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'identifier',
                                    'ty': '*i8',
                                    'value': 'p2',
                                }
                            ]
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'x',
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
                                'value': 'x',
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
                                'value': 'x',
                                'ty': 'i32'
                            },
                            'op': '=',
                            'right': {
                                'kind': 'literal',
                                'ty': 'i32',
                                'value': 1
                            }
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 's',
                        'ty': '*i8',
                        'value': {
                            'kind': 'literal',
                            'ty': '*i8',
                            'value': 'null'
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def f(*i8) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'identifier',
                                    'ty': '*i8',
                                    'value': 's',
                                }
                            ]
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': '*i8',
                            'left': {
                                'kind': 'identifier',
                                'ty': '*i8',
                                'value': 'p2',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': '*i8',
                                'value': 's',
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
