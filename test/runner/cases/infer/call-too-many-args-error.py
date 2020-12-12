from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, expected_errors=[
            self.simple_error(5, 5, "Expected 0 arguments, but got 1", self.kantan_filename())
        ])
        self.options.append('--dump-ast')
