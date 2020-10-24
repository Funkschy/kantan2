from runner.testcase import ErrorTestCase


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.note_error(lnr=1, col=8, msg='Could not scan token', notes=[
                self.simple_note('unknown token')
            ]),
            self.note_error(lnr=4, col=6, msg='Could not scan token', notes=[
                self.simple_note('invalid char literal')
            ]),
            self.note_error(lnr=5, col=8, msg='Could not scan token', notes=[
                self.simple_note('invalid escape sequence')
            ]),
        ])
