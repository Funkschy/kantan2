from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_ir = [{
    'path': kantan_filename(__file__),
    'functions': [
        {
            'kind': 'definition',
            'original_name': 'main',
            'mangled_name': '',
            'ty': 'def main() -> i32',
            'locals': [
                {
                    'name': '_1',
                    'type': 'i32',
                    'temp': False
                },
                {
                    'name': '_2',
                    'type': '*i32',
                    'temp': False
                },
                {
                    'name': '_3',
                    'type': 'i32',
                    'temp': False
                },
            ],
            'blocks': {
                'bb0': {
                    'statements': [
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_1',
                                'temp': False,
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
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
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_2',
                                'temp': False,
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': '*i32',
                                    'value': {
                                        'kind': 'undefined'
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_3',
                                'temp': False,
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'i32',
                                    'value': {
                                        'kind': 'int',
                                        'value': 2
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_2',
                                'temp': False,
                                'projections': []
                            },
                            'value': {
                                'kind': 'ref',
                                'location': {
                                    'kind': 'local',
                                    'name': '_3',
                                    'temp': False,
                                    'projections': []
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_2',
                                'temp': False,
                                'projections': [
                                    {'kind': 'deref'}
                                ]
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'copy',
                                    'location': {
                                        'kind': 'local',
                                        'name': '_1',
                                        'temp': False,
                                        'projections': []
                                    }
                                }
                            }
                        },
                    ],
                    'terminator': {
                        'kind': 'return',
                        'operand': {
                            'kind': 'copy',
                            'location': {
                                'kind': 'local',
                                'name': '_2',
                                'temp': False,
                                'projections': [
                                    {'kind': 'deref'}
                                ]
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
