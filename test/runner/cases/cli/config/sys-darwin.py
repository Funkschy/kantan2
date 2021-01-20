from typing import List, Optional

from runner.output import Output
from runner.testcase import TestError, expected_but_got, SuccessTestCase

expected = 'x86_64-apple-darwin'


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options = ['--mi', '--dump-config', '--sys', 'darwin']

    def test_output(self, output: Output) -> Optional[TestError]:
        if output.config['target'] != expected:
            return expected_but_got('error', expected, output.config['target'])
        return None

    def files(self) -> List[str]:
        return []
