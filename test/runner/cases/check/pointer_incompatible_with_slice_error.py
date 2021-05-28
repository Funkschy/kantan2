from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=4, col=7, msg='Invalid operator \'-\' for types \'[]i8\' and \'*i8\''),
        ])
