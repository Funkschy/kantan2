from runner.testcase import ErrorTest


class Test(ErrorTest):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=0, col=0, msg='no kantan files', file='')
        ])

    def files(self):
        return []
