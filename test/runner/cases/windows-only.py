from runner import env
from runner.execute import PredicateCompilerExecutor

from runner.testcase import SuccessTestCase


# Felix: this test case is just a proof of concept, because i will definitely forget how to use my own library
class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(PredicateCompilerExecutor(executor, [lambda: env.get_os_name() == 'Windows']))
