from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, expected_errors=[
            self.simple_error(1, 6, 'An empty list of generics is invalid')
        ])
