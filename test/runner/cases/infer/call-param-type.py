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
            "instances": ["(*i8, isize) -> void"],
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
                        "kind": "local_var_decl",
                        "name": "s",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": "null"
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "len",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": 0
                        }
                    },
                    {
                        "kind": "expr_stmt",
                        "expr": {
                            "kind": "call",
                            "callee": {
                                "kind": "identifier",
                                "value": "f",
                                "ty": "(*i8, isize) -> void"
                            },
                            "args": [
                                {
                                    "kind": "identifier",
                                    "value": "s",
                                    "ty": "*i8"
                                },
                                {
                                    "kind": "identifier",
                                    "value": "len",
                                    "ty": "isize"
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
