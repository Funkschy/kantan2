from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename, relative_filename

expected_ir = [
    {
        "path": kantan_filename(__file__),
        "functions": [
            {
                "kind": "definition",
                "original_name": "some_function",
                "mangled_name": "",
                "ty": "def some_function() -> i32",
                "locals": [],
                "blocks": {
                    "bb0": {
                        "statements": [],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "constant",
                                "type": "i32",
                                "value": {
                                    "kind": "int",
                                    "value": 0
                                }
                            }
                        }
                    }
                }
            },
            {
                "kind": "definition",
                "original_name": "main",
                "mangled_name": "",
                "ty": "def main() -> i32",
                "locals": [
                    {
                        "name": "_1",
                        "type": "i32",
                        "temp": True
                    },
                    {
                        "name": "_2",
                        "type": "i32",
                        "temp": True
                    },
                    {
                        "name": "_3",
                        "type": "i32",
                        "temp": True
                    }
                ],
                "blocks": {
                    "bb0": {
                        "statements": [],
                        "terminator": {
                            "kind": "call",
                            "callee": {
                                "kind": "constant",
                                "type": "() -> i32",
                                "value": {
                                    "kind": "function",
                                    "name": "some_function",
                                    'declared_in': relative_filename(__file__, '../helper/function.kan'),
                                }
                            },
                            "args": [],
                            "dest": {
                                "kind": "local",
                                "name": "_1",
                                "temp": True,
                                "projections": []
                            },
                            "next": "bb1"
                        }
                    },
                    "bb1": {
                        "statements": [],
                        "terminator": {
                            "kind": "call",
                            "callee": {
                                "kind": "constant",
                                "type": "() -> i32",
                                "value": {
                                    "kind": "function",
                                    "name": "some_function",
                                    'declared_in': kantan_filename(__file__)
                                }
                            },
                            "args": [],
                            "dest": {
                                "kind": "local",
                                "name": "_2",
                                "temp": True,
                                "projections": []
                            },
                            "next": "bb2"
                        }
                    },
                    "bb2": {
                        "statements": [
                            {
                                "kind": "assignment",
                                "location": {
                                    "kind": "local",
                                    "name": "_3",
                                    "temp": True,
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
                                            "temp": True,
                                            "projections": []
                                        }
                                    },
                                    "right": {
                                        "kind": "copy",
                                        "location": {
                                            "kind": "local",
                                            "name": "_2",
                                            "temp": True,
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
                                    "temp": True,
                                    "projections": []
                                }
                            }
                        }
                    }
                }
            }
        ]
    },
    {
        'path': relative_filename(__file__, '../helper/function.kan'),
        "functions": [
            {
                "kind": "definition",
                "original_name": "some_function",
                "mangled_name": "",
                "ty": "def some_function() -> i32",
                "locals": [],
                "blocks": {
                    "bb0": {
                        "statements": [],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "constant",
                                "type": "i32",
                                "value": {
                                    "kind": "int",
                                    "value": 0
                                }
                            }
                        }
                    }
                }
            }
        ]
    }
]


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options.append('--dump-ir')

    def test_output(self, output: Output) -> Optional[TestError]:
        super_error = super().test_output(output)
        if super_error is not None:
            return super_error

        ir = output.ir
        if ir != expected_ir:
            return expected_but_got('ir', expected_ir, ir)
