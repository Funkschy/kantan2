from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

from ctypes import c_void_p, sizeof

pointer_width = sizeof(c_void_p)

expected_ir = [{
    'path': kantan_filename(__file__),
    'functions': [
        {
            'original_name': 'main',
            'locals': [
                {
                    'name': '_1',
                    'type': 'usize'
                },
                {
                    'name': '_2',
                    'type': 'usize'
                },
                {
                    'name': '_3',
                    'type': 'usize'
                },
                {
                    'name': '_4',
                    'type': 'usize'
                },
                {
                    'name': '_5',
                    'type': 'usize'
                },
                {
                    'name': '_6',
                    'type': 'usize'
                },
                {
                    'name': '_7',
                    'type': 'usize'
                },
                {
                    'name': '_8',
                    'type': 'usize'
                },
                {
                    'name': '_9',
                    'type': 'usize'
                },
                {
                    'name': '_10',
                    'type': 'usize'
                },
                {
                    'name': '_11',
                    'type': 'usize'
                },
                {
                    'name': '_12',
                    'type': 'usize'
                },
                {
                    'name': '_13',
                    'type': 'usize'
                },
                {
                    'name': '_14',
                    'type': 'usize'
                },
                {
                    'name': '_15',
                    'type': 'usize'
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
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 1
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
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 1
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
                                    'type': 'usize',
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
                                'name': '_4',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 4
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_5',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 8
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_6',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': pointer_width
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_7',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 1
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_8',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
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
                                'name': '_9',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 4
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_10',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 8
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_11',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': pointer_width
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_12',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 4
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_13',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 8
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_14',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': pointer_width
                                    }
                                }
                            }
                        },
                        {
                            'kind': 'assignment',
                            'location': {
                                'kind': 'local',
                                'name': '_15',
                                'projections': []
                            },
                            'value': {
                                'kind': 'use',
                                'operand': {
                                    'kind': 'constant',
                                    'type': 'usize',
                                    'value': {
                                        'kind': 'int',
                                        'value': 2 * pointer_width
                                    }
                                }
                            }
                        },
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
