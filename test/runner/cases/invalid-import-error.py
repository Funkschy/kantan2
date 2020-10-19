from pathlib import Path

from runner.testcase import ErrorTest


def get_import_path() -> str:
    parent_dir = Path(__file__).parent
    return str(parent_dir) + '/other-module.kan'


class Test(ErrorTest):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=2, col=1, msg='Expected \';\', but got \'import\''),
            self.note_error(lnr=3, col=9, msg='Invalid import: could not find \'other-module\'', notes=[
                self.simple_note(f'the resolved path was \'{get_import_path()}\'')
            ]),
            self.simple_error(lnr=4, col=8, msg='Expected \'string literal\', but got \'undefined\'')
        ])
