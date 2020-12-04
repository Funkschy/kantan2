from os.path import splitext

from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=0, col=0, msg=f'could not find \'{splitext(__file__)[0]}.kan\'', file='')
        ])
