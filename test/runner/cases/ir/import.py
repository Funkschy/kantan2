from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename, relative_filename

expected_ir = [
    {
        'path': kantan_filename(__file__),
        'functions': [
            {
                'kind': 'definition',
                'original_name': 'main',
                'mangled_name': '',
                'ty': 'def main() -> void',
                'locals': [],
                'blocks': {
                    'bb0': {
                        'statements': [],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "constant",
                                "type": "void",
                                "value": None
                            }
                        }
                    },
                }
            },
        ]
    },
    {
        'path': relative_filename(__file__, '../helper/some-function.kan'),
        'functions': [
            {
                'kind': 'definition',
                'original_name': 'some_function',
                'mangled_name': '',
                'ty': 'def some_function() -> i32',
                'locals': [],
                'blocks': {
                    'bb0': {
                        'statements': [],
                        "terminator": {
                            "kind": "return",
                            'operand': {
                                'kind': 'constant',
                                'type': 'i32',
                                'value': {
                                    'kind': 'int',
                                    'value': 0
                                }
                            }
                        }
                    },
                }
            },
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
