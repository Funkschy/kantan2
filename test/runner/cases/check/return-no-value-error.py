from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=5, msg='Expected \'i32\', but got \'no return value\''),
        ])
