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
                "def f([]i8, i32, i8) -> []i8",
                "def f([]i8, i8, i32) -> []i8",
                "def f(i32, []i8, i8) -> i32",
                "def f(i32, i8, []i8) -> i32",
                "def f(i8, []i8, i32) -> i8",
                "def f(i8, i32, []i8) -> i8"
            ],
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i8, i32, []i8) -> i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i8, []i8, i32) -> i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i32",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i32, i8, []i8) -> i32",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i32",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i32, []i8, i8) -> i32",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f([]i8, i8, i32) -> []i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f([]i8, i32, i8) -> []i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "a"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "return",
                        "value": {
                            "kind": "identifier",
                            "ty": "i8",
                            "value": "a"
                        }
                    }
                ]
            }
        },
        {
            "kind": "func_def",
            "name": "f2",
            "instances": [
                "def f2([]i8, i32, i8) -> []i8"
            ],
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f([]i8, i32, i8) -> []i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f([]i8, i8, i32) -> []i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i32",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i32, []i8, i8) -> i32",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i32",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i32, i8, []i8) -> i32",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i8, []i8, i32) -> i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f(i8, i32, []i8) -> i8",
                                "value": "f"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "ty": "i8",
                                    "value": "c"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "b"
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "[]i8",
                                    "value": "a"
                                }
                            ]
                        }
                    },
                    {
                        "kind": "return",
                        "value": {
                            "kind": "identifier",
                            "ty": "[]i8",
                            "value": "a"
                        }
                    }
                ]
            }
        },
        {
            "kind": "func_def",
            "name": "main",
            "instances": [
                "def main() -> void"
            ],
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "local_var_decl",
                        "name": "i",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "ty": "i32",
                            "value": 1
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "j",
                        "ty": None,
                        "value": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f2([]i8, i32, i8) -> []i8",
                                "value": "f2"
                            },
                            "args": [
                                {
                                    "kind": "literal",
                                    "ty": "[]i8",
                                    "value": ""
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "i"
                                },
                                {
                                    "kind": "literal",
                                    "ty": "i8",
                                    "value": " "
                                }
                            ]
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f2([]i8, i32, i8) -> []i8",
                                "value": "f2"
                            },
                            "args": [
                                {
                                    "kind": "literal",
                                    "ty": "[]i8",
                                    "value": ""
                                },
                                {
                                    "kind": "literal",
                                    "ty": "i32",
                                    "value": 0
                                },
                                {
                                    "kind": "literal",
                                    "ty": "i8",
                                    "value": " "
                                }
                            ]
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "k",
                        "ty": None,
                        "value": {
                            "kind": "identifier",
                            "ty": "i32",
                            "value": "i"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "ty": "[]i8",
                            "callee": {
                                "kind": "identifier",
                                "ty": "def f2([]i8, i32, i8) -> []i8",
                                "value": "f2"
                            },
                            "args": [
                                {
                                    "kind": "literal",
                                    "ty": "[]i8",
                                    "value": ""
                                },
                                {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "k"
                                },
                                {
                                    "kind": "literal",
                                    "ty": "i8",
                                    "value": " "
                                }
                            ]
                        }
                    },
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
