from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=5, msg='Could not infer type'),
            self.simple_error(lnr=3, col=5, msg='Could not infer type')
        ])
