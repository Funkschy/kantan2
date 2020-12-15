from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=16, msg="No identifier 'not_defined' in scope"),
            self.simple_error(lnr=4, col=5, msg="No identifier 'not_defined' in scope"),
        ])
