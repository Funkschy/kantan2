import subprocess
from pathlib import Path
from typing import List, Optional

from runner.output import Output, parse_output

error_rc = 255
segfault_rc = -11
abort_rc = -6


def valgrind(filename: str, suppress_path: Optional[str]) -> List[str]:
    cmd = ['valgrind']

    if suppress_path is not None:
        cmd += [f'--suppressions={suppress_path}']

    return cmd + [
        '--leak-check=full',
        '--error-exitcode=' + str(error_rc),
        '--xml=yes',
        '--xml-file={}.xml'.format(filename)
    ]


class ValgrindOptions(object):
    def __init__(self, use_valgrind: bool, suppress_file: str):
        self.use_valgrind = use_valgrind
        self.suppress_file = suppress_file


# actually runs the compiler
class CompilerExecutor(object):
    def __init__(self, compiler_path: str, valgrind_opts: ValgrindOptions):
        self.compiler_path = compiler_path
        self.valgrind_opts = valgrind_opts

    def _run(self, filename: str, files: List[str], options: List[str]) -> subprocess.CompletedProcess:
        cmd = [self.compiler_path] + options + files
        if self.valgrind_opts.use_valgrind:
            cmd = valgrind(filename, self.valgrind_opts.suppress_file) + cmd

        return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Path.cwd())

    def run(self, filename: str, files: List[str], options: List[str]) -> Optional[Output]:
        completed_process = self._run(filename, files, options)
        return parse_output(completed_process)


class PredicateCompilerExecutor(CompilerExecutor):
    def __init__(self, base: CompilerExecutor, predicates):
        super().__init__(base.compiler_path, base.valgrind_opts)
        self.predicates = predicates

    def run(self, filename: str, files: List[str], options: List[str]) -> Optional[Output]:
        for predicate in self.predicates:
            if not predicate():
                return None

        return super().run(filename, files, options)


class NonParsingExecutor(CompilerExecutor):
    def __init__(self, base: CompilerExecutor):
        super().__init__(base.compiler_path, base.valgrind_opts)

    def run(self, filename: str, files: List[str], options: List[str]) -> Optional[str]:
        completed_process = self._run(filename, files, options)
        return completed_process.stdout.decode('utf-8')
