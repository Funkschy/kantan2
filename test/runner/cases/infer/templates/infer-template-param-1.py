from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    'kind': 'module',
    'path': kantan_filename(__file__),
    'imports': [],
    'items': [
        {
            "kind": "func_def",
            "name": "f",
            "instances": [
                "(i32) -> void",
                "(f32) -> void",
                "(u32) -> void"
            ],
            "body": {
                "kind": "block",
                "stmts": []
            }
        },
        {
            "kind": "func_def",
            "name": "main",
            "instances": ["() -> void"],
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(i32) -> void"
                            },
                            "args": [
                                {
                                    "kind": "literal",
                                    "value": 1
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(f32) -> void"
                            },
                            "args": [
                                {
                                    "kind": "literal",
                                    "value": 1
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "x",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "undefined"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(u32) -> void"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "x",
                                    "ty": "u32"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "u",
                        "ty": "u32",
                        "value": {
                            "kind": "literal",
                            "value": 0
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "assign",
                            "left": {
                                "kind": "identifier",
                                "value": "x",
                                "ty": "u32"
                            },
                            "op": "=",
                            "right": {
                                "kind": "identifier",
                                "value": "u",
                                "ty": "u32"
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
