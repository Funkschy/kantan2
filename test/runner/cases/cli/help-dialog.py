from typing import Optional

from runner.execute import NonParsingExecutor
from runner.testcase import TestCase, TestError, expected_but_got

expected = '''kantan
Felix Schoeller <felix.schoeller@protonmail.com>
The official compiler for the Kantan programming language

USAGE:
    kantan [OPTIONS] <source-file>...

OPTIONS:
    --help / -h               print this help text
    --debug-symbols / -g      enable debug symbols in the output
    --mi                      enable the machine interface               (output everything as json)
    --dump-ast                dump the ast as json                       (needs --mi)
    --dump-config             dump the compiler config as json           (needs --mi)
    --dump-type-graph         dump the type-graph as json                (needs --mi)
    --dump-ir                 dump the ir as json                        (needs --mi)
    --parse-only              quit after parsing
    --opt-level / -O <level>  the optimization level                     [possible values: 0, 1, 2, 3]
    --out / -o <file>         the output file                            (end with .s/.o for assembly/obj-file output)
    --target <argument>       set the target <arch>-<vendor>-<sys>-<abi> (see --print-available-targets)
    --print-available-targets print all available target triples

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
