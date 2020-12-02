from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=15, msg='No type \'test\' in scope'),
        ])
