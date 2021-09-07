from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            # TODO: this error should not be reported twice
            self.simple_error(lnr=1, col=9, msg='Could not infer type'),
            self.simple_error(lnr=1, col=9, msg='Could not infer type'),
        ])
