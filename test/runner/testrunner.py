import importlib.util as util
import os
import sys
from enum import Enum
from os.path import splitext
from typing import Optional

from runner.execute import CompilerExecutor, ExecutionError
from runner.output import Output


class TermColor:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colored(color, text):
    return color + text + TermColor.ENDC


class Result(object):
    class Status(Enum):
        Success = colored(TermColor.OKGREEN, 'SUCCESS'), colored(TermColor.OKGREEN, 'SUCCESSFUL: ')
        Failure = colored(TermColor.FAIL, 'FAILURE'), colored(TermColor.FAIL, 'FAILED: ')
        Skipped = colored(TermColor.WARNING, 'SKIPPED'), colored(TermColor.WARNING, 'SKIPPED: ')

    def __init__(self, status: Status, py_filename: str, msg: Optional[str] = None):
        self.status = status
        self.py_filename = py_filename
        self.msg = msg


class TestRunner(object):
    def __init__(self, default_executor: CompilerExecutor, py_filename: str):
        self.py_filename = py_filename
        self.default_executor = default_executor

    def run(self, print_output_on_fail: bool) -> Result:
        modname = splitext(self.py_filename)[0].replace('/', '.')
        spec = util.spec_from_file_location(modname, self.py_filename)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[modname] = module

        test = module.Test(self.default_executor)

        output = None
        try:
            output = test.run()
            if output is None:
                return Result(Result.Status.Skipped, self.py_filename)

            if type(output) is ExecutionError:
                if print_output_on_fail:
                    print(output.raw)
                return Result(Result.Status.Failure, self.py_filename, output.msg)

            error = test.test_output(output)
            if error is not None:
                if print_output_on_fail:
                    print(output.raw if type(output) is Output else output)
                return Result(Result.Status.Failure, self.py_filename, error.msg)

        except Exception as e:
            if output is not None and print_output_on_fail:
                print(output.raw if type(output) is Output else output)
            return Result(Result.Status.Failure, self.py_filename, str(e))

        return Result(Result.Status.Success, self.py_filename)
