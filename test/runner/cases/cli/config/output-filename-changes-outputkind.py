from typing import List, Optional

from runner.output import Output
from runner.testcase import TestError, expected_but_got, SuccessTestCase


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options = ['--mi', '--dump-config', '-o', 'test.s']

    def test_output(self, output: Output) -> Optional[TestError]:
        # this does not have a separate test, since all tests use json output
        if output.config['error-output-format'] != 'json':
            return expected_but_got('error', 'json', output.config['error-output-format'])

        if output.config['output-kind'] != 'asm':
            return expected_but_got('error', 'asm', output.config['output-kind'])

        if output.config['invoke-linker']:
            return expected_but_got('error', 'no linker invocation', 'linker invocation')

        return None

    def files(self) -> List[str]:
        return []
