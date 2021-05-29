from os.path import realpath, dirname
from pathlib import Path
from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_ir = [
    {
        'path': kantan_filename(__file__),
        'functions': [
            {
                'original_name': 'main',
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
        'path': realpath(Path(dirname(Path(kantan_filename(__file__)))).joinpath(Path('../helper/some-function.kan'))),
        'functions': [
            {
                'original_name': 'some_function',
                'locals': [
                    {
                        'name': '_1',
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
                                            'kind': 'int',
                                            'value': 0
                                        }
                                    }
                                }
                            }
                        ],
                        "terminator": {
                            "kind": "return",
                            "operand": {
                                "kind": "copy",
                                'location': {
                                    'kind': 'local',
                                    'name': '_1',
                                    'projections': []
                                },
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
