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
                'def f() -> bool',
                'def f() -> u32'
            ],
            'body': {
                'kind': 'block',
                'stmts': []
            }
        },
        {
            'kind': 'func_def',
            'name': 'g',
            'instances': [
                'def g(u32) -> u32'
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
                        'name': 'x',
                        'ty': None,
                        'value': {
                            'kind': 'call',
                            'ty': 'bool',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def f() -> bool',
                                'value': 'f',
                            },
                            'args': []
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'unary',
                            'ty': 'bool',
                            'op': '!',
                            'right': {
                                'kind': 'identifier',
                                'ty': 'bool',
                                'value': 'x',
                            }
                        }
                    },
                    {
                        'kind': 'local_var_decl',
                        'name': 'u',
                        'ty': 'u32',
                        'value': {
                            'kind': 'call',
                            'ty': 'u32',
                            'callee': {
                                'kind': 'identifier',
                                'ty': 'def g(u32) -> u32',
                                'value': 'g',
                            },
                            'args': [
                                {
                                    'kind': 'call',
                                    'ty': 'u32',
                                    'callee': {
                                        'kind': 'identifier',
                                        'ty': 'def f() -> u32',
                                        'value': 'f',
                                    },
                                    'args': []
                                }
                            ]
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
