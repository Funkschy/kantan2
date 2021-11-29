from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename, relative_filename

expected_modules = [
    {
        'kind': 'module',
        'path': kantan_filename(__file__),
        'imports': [
            {
                'path': relative_filename(__file__, '../../helper/mod-with-template.kan'),
                'alias': 'mod_with_template'
            }
        ],
        "items": [
            {
                "kind": "func_def",
                "name": "main",
                "instances": [
                    "def main() -> void",
                ],
                "body": {
                    "kind": "block",
                    "stmts": [
                        {
                            "kind": "expr_stmt",
                            "expr": {
                                "kind": "call",
                                "ty": "i32",
                                "callee": {
                                    'kind': 'access',
                                    'ty': 'def f(i32) -> i32',
                                    'left': {
                                        'kind': 'identifier',
                                        'ty': 'module',
                                        'value': 'mod_with_template'
                                    },
                                    'ident': {
                                        'kind': 'identifier',
                                        'ty': 'def f(i32) -> i32',
                                        'value': 'f'
                                    }
                                },
                                "args": [
                                    {
                                        "kind": "literal",
                                        "ty": "i32",
                                        "value": 1
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        ]
    },
    {
        'kind': 'module',
        'path': relative_filename(__file__, '../../helper/mod-with-template.kan'),
        'imports': [],
        "items": [
            {
                "kind": "func_def",
                "name": "f",
                "instances": [
                    "def f(i32) -> i32",
                ],
                "body": {
                    "kind": "block",
                    "stmts": [
                        {
                            'kind': 'return',
                            'value': {
                                'kind': 'identifier',
                                'ty': 'i32',
                                'value': 't'
                            }
                        }
                    ]
                }
            }
        ]
    }
]


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
