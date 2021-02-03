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
                '(i32) -> void',
                '(f32) -> void',
                '(u32) -> void'
            ],
            'body': {
                'kind': 'block',
                'stmts': []
            }
        },
        {
            'kind': 'func_def',
            'name': 'main',
            'instances': ['() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': '(i32) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'literal',
                                    'ty': 'i32',
                                    'value': 1
                                }
                            ]
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'call',
                            'ty': 'void',
                            'callee': {
                                'kind': 'identifier',
                                'ty': '(f32) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'literal',
                                    'ty': 'f32',
                                    'value': 1
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
                            'ty': 'u32',
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
                                'ty': '(u32) -> void',
                                'value': 'f',
                            },
                            'args': [
                                {
                                    'kind': 'identifier',
                                    'ty': 'u32',
                                    'value': 'x',
                                }
                            ]
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
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'assign',
                            'ty': 'u32',
                            'left': {
                                'kind': 'identifier',
                                'ty': 'u32',
                                'value': 'x',
                            },
                            'op': '=',
                            'right': {
                                'kind': 'identifier',
                                'ty': 'u32',
                                'value': 'u',
                            }
                        }
                    }]

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
