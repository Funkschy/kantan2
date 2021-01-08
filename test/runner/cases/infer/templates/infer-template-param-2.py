from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    'kind': 'module',
    'path': kantan_filename(__file__),
    'imports': [],
    "items": [
        {
            "kind": "func_def",
            "name": "f",
            "instances": [
                "(*i32) -> void",
                "(*i8) -> void"
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
                        "name": "p",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "null"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(*i32) -> void"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "p",
                                    "ty": "*i32"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "p2",
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
                                "ty": "(*i8) -> void"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "p2",
                                    "ty": "*i8"
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
                            "kind": "assign",
                            "left": {
                                "kind": "unary",
                                "op": "*",
                                "right": {
                                    "kind": "identifier",
                                    "value": "p",
                                    "ty": "*i32"
                                }
                            },
                            "op": "=",
                            "right": {
                                "kind": "identifier",
                                "value": "x",
                                "ty": "i32"
                            }
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "assign",
                            "left": {
                                "kind": "identifier",
                                "value": "x",
                                "ty": "i32"
                            },
                            "op": "=",
                            "right": {
                                "kind": "literal",
                                "value": 1
                            }
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "s",
                        "ty": "*i8",
                        "value": {
                            "kind": "literal",
                            "value": "null"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(*i8) -> void"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "s",
                                    "ty": "*i8"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "assign",
                            "left": {
                                "kind": "unary",
                                "op": "*",
                                "right": {
                                    "kind": "identifier",
                                    "value": "p2",
                                    "ty": "*i8"
                                }
                            },
                            "op": "=",
                            "right": {
                                "kind": "unary",
                                "op": "*",
                                "right": {
                                    "kind": "identifier",
                                    "value": "s",
                                    "ty": "*i8"
                                }
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
