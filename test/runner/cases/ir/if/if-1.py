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
            'locals': [],
            'blocks': {
                'bb0': {
                    'statements': [],
                    'terminator': {
                        'kind': 'switch',
                        'condition': {
                            'kind': 'constant',
                            'type': 'bool',
                            'value': {
                                'kind': 'bool',
                                'value': True
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
                        'target': 'bb2'
                    }
                },
                'bb2': {
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
