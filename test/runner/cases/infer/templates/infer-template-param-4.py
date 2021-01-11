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
                "(*i32) -> i32",
                "(**i32) -> *i32",
                "(*u32) -> u32"
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
                                "ty": "(*i32) -> i32"
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
                                "kind": "literal",
                                "value": 1
                            }
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
                        "kind": "local_var_decl",
                        "name": "i",
                        "ty": "i32",
                        "value": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(*i32) -> i32"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "p2",
                                    "ty": "*i32"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "p3",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "undefined"
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "i",
                        "ty": "*i32",
                        "value": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(**i32) -> *i32"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "p3",
                                    "ty": "**i32"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "p4",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "undefined"
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "i",
                        "ty": "*i32",
                        "value": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(**i32) -> *i32"
                            },
                            "args": [
                                {
                                    "kind": "unary",
                                    "op": "&",
                                    "right": {
                                        "kind": "identifier",
                                        "value": "p4",
                                        "ty": "*i32"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "i",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "undefined"
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
                                "value": "f",
                                "ty": "(*u32) -> u32"
                            },
                            "args": [
                                {
                                    "kind": "unary",
                                    "op": "&",
                                    "right": {
                                        "kind": "identifier",
                                        "value": "i",
                                        "ty": "u32"
                                    }
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
