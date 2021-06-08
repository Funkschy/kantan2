from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_ir = [{
    'path': kantan_filename(__file__),
    'functions': [
        {
            'kind': 'definition',
            'original_name': 'f',
            'mangled_name': '',
            'ty': 'def f(i32) -> i32',
            'locals': [],
            'blocks': {}
        },
        {
            'kind': 'definition',
            'original_name': 'main',
            'mangled_name': '',
            'ty': 'def main() -> void',
            'locals': [
                {
                    'name': '_1',
                    'type': 'i32'
                },
                {
                    'name': '_2',
                    'type': 'i32'
                },
                {
                    'name': '_3',
                    'type': 'i32'
                }
            ],
            'blocks': {
                'bb0': {
                    'statements': [
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_1',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'i32',
                                    'value': {
                                        'kind': 'undefined'
                                    }
                                }
                            }
                        }
                    ],
                    'terminator': {
                        'kind': 'call',
                        'callee': {
                            'kind': 'constant',
                            'type': '(i32) -> i32',
                            'value': {
                                'kind': 'function',
                                'name': 'f',
                                'declared_in': kantan_filename(__file__),
                            },
                        },
                        'args': [],
                        'dest': {
                            'kind': 'local',
                            'name': '_3',
                            'projections': []
                        },
                        'next': 'bb1'
                    }
                },
                'bb1': {
                    'statements': [
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_2',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'copy',
                                    'location': {
                                        'kind': 'local',
                                        'name': '_3',
                                        'projections': []
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
    ]
}]


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
