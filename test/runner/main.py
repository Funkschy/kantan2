#!/usr/bin/env python3

import argparse
import multiprocessing
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from os import listdir
from os.path import splitext, basename, abspath, join, isfile
from typing import List, Set

from runner.execute import CompilerExecutor, ValgrindOptions
from runner.testrunner import TestRunner, Result


def main():
    parser = argparse.ArgumentParser(
        description='The Kantan test runner',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('compiler', type=str, help='path to the compiler executable')
    parser.add_argument('tests', type=str, help='path to the test files directory')
    parser.add_argument('--valgrind', action='store_true', help='use valgrind to check for memory leaks')
    parser.add_argument('--suppress', type=str, default=None, help='path to valgrind suppress file')
    parser.add_argument('--threads', type=int, default=multiprocessing.cpu_count() * 2, help='number of worker threads')
    parser.add_argument('--show-skipped', action='store_true', help='also print info for skipped tests')
    parser.add_argument('--print-fail-output', action='store_true',
                        help='print the raw compiler output for failed tests')

    args = parser.parse_args()
    state = State(args.show_skipped, args.print_fail_output)

    default_executor = CompilerExecutor(args.compiler, ValgrindOptions(args.valgrind, args.suppress))
    tests = read(args.tests, default_executor)

    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        pool.map(lambda runner: run_test_case(runner, state), tests)

    print(Result.Status.Success.value[1], state.successful)
    if state.failures > 0:
        print(Result.Status.Failure.value[1], state.failures)
    if state.skipped > 0 and state.show_skipped:
        print(Result.Status.Skipped.value[1], state.skipped)

    if len(tests) != state.successful + state.skipped + state.failures:
        # this can happen, if the test itself contained python errors
        print("Some tests could not be executed")


def run_test_case(runner: TestRunner, state):
    result = runner.run(state.print_fail_output)
    state.add(result.status)

    if result.status == Result.Status.Skipped and not state.show_skipped:
        return

    print(result.status.value[0], ':', result.py_filename, '' if result.msg is None else f': {result.msg}')


class State(object):
    def __init__(self, show_skipped: bool, print_fail_output: bool):
        self.print_fail_output = print_fail_output
        self.show_skipped = show_skipped
        self.failures = 0
        self.successful = 0
        self.skipped = 0
        self.failure_lock = threading.Lock()
        self.success_lock = threading.Lock()
        self.skip_lock = threading.Lock()

    def add(self, status: Result.Status):
        if status == Result.Status.Success:
            self.add_success()
        elif status == Result.Status.Skipped:
            self.add_skipped()
        elif status == Result.Status.Failure:
            self.add_failure()

    def add_failure(self):
        self.failure_lock.acquire()
        self.failures += 1
        self.failure_lock.release()

    def add_success(self):
        self.success_lock.acquire()
        self.successful += 1
        self.success_lock.release()

    def add_skipped(self):
        self.skip_lock.acquire()
        self.skipped += 1
        self.skip_lock.release()


def read(test_path: str, default_executor: CompilerExecutor) -> List[TestRunner]:
    ignored = read_ignored(test_path)

    def add_file(f) -> bool:
        st = splitext(f)
        return st[1] == '.py' and basename(st[0]) not in ignored

    files = filter(add_file, [abspath(join(test_path, f)) for f in listdir(test_path)])
    return [TestRunner(default_executor, path) for path in files]


def read_ignored(test_path: str) -> Set[str]:
    ignore_file = join(test_path, 'kantan-test-ignore')
    if not isfile(ignore_file):
        return set()

    with open(ignore_file) as f:
        return set(map(lambda n: n.strip(), f.readlines()))


if __name__ == '__main__':
    main()
