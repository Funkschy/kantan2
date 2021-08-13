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
            'ty': 'def f(bool, bool, bool) -> i32',
            'locals': [
                {
                    "name": "_1",
                    "type": "bool",
                    "temp": False
                },
                {
                    "name": "_2",
                    "type": "bool",
                    "temp": False
                },
                {
                    "name": "_3",
                    "type": "bool",
                    "temp": False
                }
            ],
            'blocks': {
                'bb0': {
                    'statements': [],
                    'terminator': {
                        'kind': 'switch',
                        'condition': {
                            "kind": "copy",
                            "location": {
                                "kind": "local",
                                "name": "_1",
                                "temp": False,
                                "projections": []
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
                            "kind": "copy",
                            "location": {
                                "kind": "local",
                                "name": "_2",
                                "temp": False,
                                "projections": []
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
                            "kind": "copy",
                            "location": {
                                "kind": "local",
                                "name": "_3",
                                "temp": False,
                                "projections": []
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
                            "kind": "nop",
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
