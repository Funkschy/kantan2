from typing import List, Optional

from runner import env
from runner.execute import PredicateCompilerExecutor
from runner.output import Output
from runner.testcase import TestError, expected_but_got, SuccessTestCase

expected = 'x86_64-unknown-linux-sysv'


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(PredicateCompilerExecutor(executor, [lambda: env.get_os_name() == 'Linux']))
        self.options = ['--mi', '--dump-config', '--sys', 'linux']

    def test_output(self, output: Output) -> Optional[TestError]:
        if not output.config['invoke-linker']:
            return expected_but_got('error', 'linker invocation', 'no linker invocation')
        return None

    def files(self) -> List[str]:
        return []
