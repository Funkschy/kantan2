from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=3, col=12, msg='Expected \'i32\', but got \'u32\''),
        ])
