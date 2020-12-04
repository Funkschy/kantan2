from typing import List, Optional

from runner.execute import NonParsingExecutor
from runner.testcase import ErrorTestCase, TestError, expected_but_got

expected = 'error: --dump-ast can only be used in combination with --mi\n'


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(NonParsingExecutor(executor), [])
        self.options = ['--dump-ast']

    def test_output(self, output: str) -> Optional[TestError]:
        if output != expected:
            return expected_but_got('error', expected, output)

        return None

    def files(self) -> List[str]:
        return []
