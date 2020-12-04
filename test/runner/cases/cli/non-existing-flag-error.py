from typing import Optional

from runner.execute import NonParsingExecutor
from runner.testcase import TestCase, TestError, expected_but_got

expected = 'error: Invalid flag \'fläg\'\n'


class Test(TestCase):
    def __init__(self, executor):
        super().__init__(NonParsingExecutor(executor))
        self.options = ['--fläg']

    def files(self):
        return []

    def test_output(self, output: str) -> Optional[TestError]:
        if output != expected:
            return expected_but_got('error', expected, output)
