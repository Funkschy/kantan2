from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, expected_errors=[
            self.simple_error(6, 7, "Expected 'i32', but got '*i32'", self.kantan_filename())
        ])
