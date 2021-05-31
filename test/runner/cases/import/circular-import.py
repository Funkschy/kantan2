from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, kantan_filename, relative_to_base, expected_but_got

expected_modules = [
    {
        'kind': 'module',
        'path': kantan_filename(__file__),
        'imports': [
            {
                'path': relative_to_base(__file__, '../helper/other-circular-import.kan'),
                'alias': 'other-circular-import'
            }
        ],
        'items': []
    },
    {
        'kind': 'module',
        'path': relative_to_base(__file__, '../helper/other-circular-import.kan'),
        'imports': [
            {
                'path': kantan_filename(__file__),
                'alias': 'circular-import'
            }
        ],
        'items': []
    }
]


class Test(SuccessTestCase):
    def __init__(self, executor):
        super().__init__(executor)
        self.options.append('--dump-ast')

    def test_output(self, output: Output) -> Optional[TestError]:
        super_error = super().test_output(output)
        if super_error is not None:
            return super_error

        modules = output.modules
        if modules != expected_modules:
            return expected_but_got('modules', expected_modules, modules)
