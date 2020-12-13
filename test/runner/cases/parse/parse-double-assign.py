from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    'kind': 'module',
    'path': kantan_filename(__file__),
    'imports': [],
    'items': [
        {
            'kind': 'func_def',
            "name": "main",
            "ret": "void",
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        "kind": "local_var_decl",
                        "name": "test",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": 1
                        }
                    },
                    {
                        "kind": "local_var_decl",
                        "name": "other",
                        "ty": None,
                        "value": {
                            "kind": "literal",
                            "value": 2
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
                                "kind": "assign",
                                "left": {
                                    "kind": "identifier",
                                    "value": "other",
                                    "ty": "i32"
                                },
                                "op": "=",
                                "right": {
                                    "kind": "literal",
                                    "value": 3,
                                }
                            }
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
