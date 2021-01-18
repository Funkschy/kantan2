from typing import Optional

from runner.execute import NonParsingExecutor
from runner.testcase import TestCase, TestError, expected_but_got

expected = '''kantan
Felix Schoeller <felix.schoeller@protonmail.com>
The official compiler for the Kantan programming language

USAGE:
    kantan [OPTIONS] <source-file>...

OPTIONS:
    --help / -h <argument>          print this help text
    --debug-symbols / -g <argument> enable debug symbols in the output
    --mi <argument>                 enable the machine interface       (output everything as json)
    --dump-ast <argument>           dump the ast as json
    --dump-type-graph <argument>    dump the type-graph as json
    --parse-only <argument>         quit after parsing
    --opt-level / -O <level>        the optimization level             [possible values: 0, 1, 2, 3]
    --out / -o <file>               the output file                    (end with .s/.o for assembly/obj-file output)
    --sys <argument>                set the target OS                  [possible values: linux, win32, darwin]
    --arch <argument>               set the target Architecture        [possible values: x86_64, wasm32]

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
