from typing import Optional

from runner.output import Output
from runner.testcase import SuccessTestCase, TestError, expected_but_got, kantan_filename

expected_modules = [{
    'kind': 'module',
    'path': kantan_filename(__file__),
    'imports': [],
    'items': [
        {
            'kind': 'func_def',
            'name': 'main',
            'instances': ['() -> void'],
            'body': {
                'kind': 'block',
                'stmts': [
                    {
                        'kind': 'local_var_decl',
                        'name': 'f',
                        'ty': 'f64',
                        'value': {
                            'kind': 'literal',
                            'ty': 'f64',
                            'value': 0.0
                        }
                    },
                    {
                        'kind': 'expr_stmt',
                        'expr': {
                            'kind': 'identifier',
                            'ty': 'f64',
                            'value': 'f',
                        }
                    },
                ]
            }
        }
    ]
}]


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
