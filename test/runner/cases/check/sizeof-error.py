from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=12, msg='No type \'undeclared\' in scope'),
            self.simple_error(lnr=3, col=12, msg='The type \'void\' is unsized'),
        ])
