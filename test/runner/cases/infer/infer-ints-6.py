from pathlib import Path
from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got

expected_modules = [{
    'kind': 'module',
    'path': str(Path(__file__).parent) + '/infer-ints-6.kan',
    'items': [
        {
            "kind": "func_def",
            "name": "main",
            "ret": "void",
            "body": {
                "kind": "block",
                "stmts": [
                    {
                        "kind": "local_var_decl",
                        "name": "test",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "undefined"
                        }
                    },
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
                        "kind": "local_var_decl",
                        "name": "p2",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "null"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "assign",
                            "left": {
                                "kind": "identifier",
                                "value": "p2",
                                "ty": "*i32"
                            },
                            "op": "=",
                            "right": {
                                "kind": "identifier",
                                "value": "p",
                                "ty": "*i32"
                            }
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
                                "value": "test",
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
                                "value": "test",
                                "ty": "i32"
                            },
                            "op": "=",
                            "right": {
                                "kind": "literal",
                                "value": 0,
                            }
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "identifier",
                            "value": "p",
                            "ty": "*i32"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "identifier",
                            "value": "p2",
                            "ty": "*i32"
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "identifier",
                            "value": "test",
                            "ty": "i32"
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
