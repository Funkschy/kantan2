from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(2, 9, 'Could not infer type')
        ])
