from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=0, col=0, msg='no kantan files', file='')
        ])

    def files(self):
        return []
