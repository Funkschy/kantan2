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
            'ty': 'def f() -> void',
            'locals': [
                {
                    'name': "_1",
                    'type': "i32",
                    'temp': False,
                },
            ],
            'blocks': {
                'bb0': {
                    'statements': [
                        {
                            "kind": "assignment",
                            "location": {
                                "kind": "local",
                                "name": "_1",
                                "temp": False,
                                "projections": []
                            },
                            "value": {
                                "kind": "use",
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

                    ],
                    'terminator': {
                        'kind': 'switch',
                        'condition': {
                            "kind": "constant",
                            "type": "bool",
                            "value": {
                                "kind": "bool",
                                "value": True
                            }
                        },
                        'cases': [
                            {
                                'value': 1,
                                'target': 'bb1'
                            },
                            {
                                'value': 0,
                                'target': 'bb2'
                            }
                        ]
                    }
                },
                'bb1': {
                    'statements': [
                        {
                            'kind': 'nop'
                        }
                    ],
                    'terminator': {
                        'kind': 'jmp',
                        'target': 'bb7'
                    }
                },
                'bb2': {
                    'statements': [],
                    'terminator': {
                        'kind': 'switch',
                        'condition': {
                            "kind": "constant",
                            "type": "bool",
                            "value": {
                                "kind": "bool",
                                "value": False
                            }
                        },
                        'cases': [
                            {
                                'value': 1,
                                'target': 'bb3'
                            },
                            {
                                'value': 0,
                                'target': 'bb4'
                            }
                        ]
                    }
                },
                'bb3': {
                    'statements': [
                        {
                            'kind': 'nop'
                        }
                    ],
                    'terminator': {
                        'kind': 'jmp',
                        'target': 'bb7'
                    }
                },
                'bb4': {
                    'statements': [],
                    'terminator': {
                        'kind': 'switch',
                        'condition': {
                            "kind": "constant",
                            "type": "bool",
                            "value": {
                                "kind": "bool",
                                "value": False
                            }
                        },
                        'cases': [
                            {
                                'value': 1,
                                'target': 'bb5'
                            },
                            {
                                'value': 0,
                                'target': 'bb6'
                            }
                        ]
                    }
                },
                'bb5': {
                    'statements': [
                        {
                            'kind': 'nop'
                        }
                    ],
                    'terminator': {
                        'kind': 'jmp',
                        'target': 'bb7'
                    }
                },
                'bb6': {
                    'statements': [
                        {
                            "kind": "assignment",
                            "location": {
                                "kind": "local",
                                "name": "_1",
                                "temp": False,
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
                        }
                    ],
                    'terminator': {
                        'kind': 'jmp',
                        'target': 'bb7'
                    }
                },
                'bb7': {
                    'statements': [
                        {
                            'kind': 'nop'
                        }
                    ],
                    'terminator': {
                        'kind': 'return',
                        'operand': {
                            'kind': 'constant',
                            'type': 'void',
                            'value': None
                        }
                    }
                },
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
