from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    "kind": "module",
    "path": kantan_filename(__file__),
    "imports": [],
    "items": [
        {
            "kind": "func_def",
            "name": "f",
            "instances": [
                "() -> bool",
                "() -> u32"
            ],
            "body": {
                "kind": "block",
                "stmts": []
            }
        },
        {
            "kind": "func_def",
            "name": "g",
            "instances": [
                "(u32) -> u32"
            ],
            "body": {
                "kind": "block",
                "stmts": []
            }
        },
        {
            "kind": "func_def",
            "name": "main",
            "instances": [
                "() -> void"
            ],
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "local_var_decl",
                        "name": "x",
                        "ty": None,
                        "value": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "() -> bool"
                            },
                            "args": []
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "unary",
                            "op": "!",
                            "right": {
                                "kind": "identifier",
                                "value": "x",
                                "ty": "bool"
                            }
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "u",
                        "ty": "u32",
                        "value": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "g",
                                "ty": "(u32) -> u32"
                            },
                            "args": [
                                {
                                    "kind": "call",
                                    "callee": {
                                        "kind": "identifier",
                                        "value": "f",
                                        "ty": "() -> u32"
                                    },
                                    "args": []
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
