from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=12, msg='Expected \'no return value\', but got \'1\''),
        ])
