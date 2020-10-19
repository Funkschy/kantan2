from runner.testcase import ErrorTest


class Test(ErrorTest):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=1, msg='Expected \';\', but got \'import\''),
            self.simple_error(lnr=3, col=9, msg='Invalid import: could not find \'other-module\''),
            self.simple_error(lnr=4, col=8, msg='Expected \'string literal\', but got \'undefined\'')
        ])
