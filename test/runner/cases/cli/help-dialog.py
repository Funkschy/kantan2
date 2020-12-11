from typing import Optional

from runner.execute import NonParsingExecutor
from runner.testcase import TestCase, TestError, expected_but_got

expected = '''kantan
Felix Schoeller <felix.schoeller@protonmail.com>
The official compiler for the Kantan programming language

USAGE:
    kantan [OPTIONS] <source-file>...

OPTIONS:
    -o <file>    the output file (end with .s for assembly output)
    -O<level>    the optimization level      [possible values 0, 1, 2, 3]
    -h / --help  print this message
    --sys        set the target OS           [possible values 'linux', 'darwin', 'win32']
    --arch       set the target Architecture [possible values 'x86_64', 'wasm32']
    --mi         output all errors/warnings as json
    --dump-ast   dump the ast as json
    --parse-only quit after parsing

ARGS:
    <source-file>...
'''


class Test(TestCase):
    def __init__(self, executor):
        super().__init__(NonParsingExecutor(executor))
        self.options = ['--help']

    def test_output(self, output: str) -> Optional[TestError]:
        if output != expected:
            return expected_but_got('help text', expected, output)

        return None
