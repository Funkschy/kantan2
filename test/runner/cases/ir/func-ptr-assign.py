from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_output = {
    "modules": [
        {
            "kind": "module",
            "path": kantan_filename(__file__),
            "imports": [],
            "items": [
                {
                    "kind": "func_def",
                    "name": "f",
                    "instances": [
                        "def f(i32) -> i32"
                    ],
                    "body": {
                        "kind": "block",
                        "stmts": [
                            {
                                "kind": "return",
                                "value": {
                                    "kind": "identifier",
                                    "ty": "i32",
                                    "value": "i"
                                }
                            }
                        ]
                    }
                },
                {
                    "kind": "func_def",
                    "name": "g",
                    "instances": [
                        "def g(i32) -> i32"
                    ],
                    "body": {
                        "kind": "block",
                        "stmts": [
                            {
                                "kind": "return",
                                "value": {
                                    "kind": "binary",
                                    "ty": "i32",
                                    "left": {
                                        "kind": "identifier",
                                        "ty": "i32",
                                        "value": "i"
                                    },
                                    "op": "+",
                                    "right": {
                                        "kind": "literal",
                                        "ty": "i32",
                                        "value": 1
                                    }
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
                                "name": "func",
                                "ty": None,
                                "value": {
                                    "kind": "identifier",
                                    "ty": "def f(i32) -> i32",
                                    "value": "f"
                                }
                            },
                            {
                                "kind": "expr_stmt",
                                "expr": {
                                    "kind": "assign",
                                    "ty": "(i32) -> i32",
                                    "left": {
                                        "kind": "identifier",
                                        "ty": "(i32) -> i32",
                                        "value": "func"
                                    },
                                    "op": "=",
                                    "right": {
                                        "kind": "identifier",
                                        "ty": "def g(i32) -> i32",
                                        "value": "g"
                                    }
                                }
                            },
                            {
                                "kind": "expr_stmt",
                                "expr": {
                                    "kind": "assign",
                                    "ty": "(i32) -> i32",
                                    "left": {
                                        "kind": "identifier",
                                        "ty": "(i32) -> i32",
                                        "value": "func"
                                    },
                                    "op": "=",
                                    "right": {
                                        "kind": "identifier",
                                        "ty": "def f(i32) -> i32",
                                        "value": "f"
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ],
    'ir': [{
        'path': kantan_filename(__file__),
        'functions': [
            {
                "kind": "definition",
                "original_name": "main",
                "mangled_name": "",
                "ty": "def main() -> void",
                "locals": [
                    {
                        "name": "_1",
                        "type": "(i32) -> i32"
                    }
                ],
                "blocks": {
                    "bb0": {
                        "statements": [
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_1",
                                    "projections": []
                                },
                                "value": {
                                    "kind": "use",
                                    "operand": {
                                        "kind": "constant",
                                        "type": "(i32) -> i32",
                                        "value": {
                                            "kind": "function",
                                            "name": "f",
                                            "declared_in": kantan_filename(__file__)
                                        }
                                    }
                                }
                            },
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_1",
                                    "projections": []
                                },
                                "value": {
                                    "kind": "use",
                                    "operand": {
                                        "kind": "constant",
                                        "type": "(i32) -> i32",
                                        "value": {
                                            "kind": "function",
                                            "name": "g",
                                            "declared_in": kantan_filename(__file__)
                                        }
                                    }
                                }
                            },
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_1",
                                    "projections": []
                                },
                                "value": {
                                    "kind": "use",
                                    "operand": {
                                        "kind": "constant",
                                        "type": "(i32) -> i32",
                                        "value": {
                                            "kind": "function",
                                            "name": "f",
                                            "declared_in": kantan_filename(__file__)
                                        }
                                    }
                                }
                            }
                        ],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "constant",
                                "type": "void",
                                "value": None
                            }
                        }
                    }
                }
            },
            {
                "kind": "definition",
                "original_name": "f",
                "mangled_name": "",
                "ty": "def f(i32) -> i32",
                "locals": [
                    {
                        "name": "_1",
                        "type": "i32"
                    }
                ],
                "blocks": {
                    "bb0": {
                        "statements": [],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "copy",
                                "location": {
                                    "kind": "local",
                                    "name": "_1",
                                    "projections": []
                                }
                            }
                        }
                    }
                }
            },
            {
                "kind": "definition",
                "original_name": "g",
                "mangled_name": "",
                "ty": "def g(i32) -> i32",
                "locals": [
                    {
                        "name": "_1",
                        "type": "i32"
                    },
                    {
                        "name": "_2",
                        "type": "i32"
                    },
                    {
                        "name": "_3",
                        "type": "i32"
                    }
                ],
                "blocks": {
                    "bb0": {
                        "statements": [
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_2",
                                    "projections": []
                                },
                                "value": {
                                    "kind": "use",
                                    "operand": {
                                        "kind": "constant",
                                        "type": "i32",
                                        "value": {
                                            "kind": "int",
                                            "value": 1
                                        }
                                    }
                                }
                            },
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_3",
                                    "projections": []
                                },
                                "value": {
                                    "kind": "binary",
                                    "binary-kind": "+",
                                    "left": {
                                        "kind": "copy",
                                        "location": {
                                            "kind": "local",
                                            "name": "_1",
                                            "projections": []
                                        }
                                    },
                                    "right": {
                                        "kind": "copy",
                                        "location": {
                                            "kind": "local",
                                            "name": "_2",
                                            "projections": []
                                        }
                                    }
                                }
                            }
                        ],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "copy",
                                "location": {
                                    "kind": "local",
                                    "name": "_3",
                                    "projections": []
                                }
                            }
                        }
                    }
                }
            }
        ]
    }]}


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options.append('--dump-ir')
        self.options.append('--dump-ast')

    def test_output(self, output: Output) -> Optional[TestError]:
        super_error = super().test_output(output)
        if super_error is not None:
            return super_error

        modules = output.modules
        if modules != expected_output['modules']:
            return expected_but_got('modules', expected_output['modules'], modules)

        ir = output.ir
        if ir != expected_output['ir']:
            return expected_but_got('ir', expected_output['ir'], ir)
