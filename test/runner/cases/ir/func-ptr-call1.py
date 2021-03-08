from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_ir = [{
    'path': kantan_filename(__file__),
    'functions': [
        {
            'original_name': 'f',
            'locals': [
                {
                    'name': '_1',
                    'type': 'u32'
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
                                    'type': 'u32',
                                    'value': {
                                        'kind': 'int',
                                        'value': 0
                                    }
                                }
                            }
                        }
                    ],
                    'terminator': {
                        'kind': 'return',
                        'operand': {
                            'kind': 'copy',
                            'location': {
                                'kind': 'local',
                                'name': '_1',
                                'projections': []
                            }
                        }
                    }
                }
            }
        },
        {
            'original_name': 'main',
            'locals': [
                {
                    'name': '_1',
                    'type': 'u32'
                },
                {
                    'name': '_2',
                    'type': 'u32'
                },
                {
                    'name': '_3',
                    'type': 'u32'
                },
                {
                    'name': '_4',
                    'type': '() -> u32'
                },
                {
                    'name': '_5',
                    'type': 'u32'
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
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'u32',
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
                                'name': '_2',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'u32',
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
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'u32',
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
                                'name': '_4',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': '() -> u32',
                                    'value': {
                                        'kind': 'function',
                                        'name': 'f'
                                    }
                                }
                            }
                        },
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
                        },
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
                                    'kind': 'copy',
                                    'location': {
                                        'kind': 'local',
                                        'name': '_2',
                                        'projections': []
                                    }
                                }
                            }
                        }
                    ],
                    'terminator': {
                        'kind': 'call',
                        'callee': {
                            'kind': 'copy',
                            'location': {
                                'kind': 'local',
                                'name': '_4',
                                'projections': []
                            }
                        },
                        'args': [],
                        'dest': {
                            'kind': 'local',
                            'name': '_5',
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
                                'name': '_1',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'copy',
                                    'location': {
                                        'kind': 'local',
                                        'name': '_5',
                                        'projections': []
                                    }
                                }
                            }
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
