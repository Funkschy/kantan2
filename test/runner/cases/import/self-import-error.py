from pathlib import Path

from runner.testcase import ErrorTestCase


def get_import_path() -> str:
    parent_dir = Path(__file__).parent
    return str(parent_dir) + '/other-module.kan'


class Test(ErrorTestCase):
    def __init__(self, executor):
        super().__init__(executor, [
            self.simple_error(lnr=1, col=9, msg='Modules cannot import themselves'),
        ])
