import json
from subprocess import CompletedProcess
from typing import List, Union


class OutputElement(object):
    def __init__(self, type: str, lnr: int, col: int, content: str, file: str, notes):
        self.notes = notes
        self.type = type
        self.lnr = lnr
        self.col = col
        self.content = content
        self.file = file

    @classmethod
    def from_json(cls, data: dict):
        elem = cls(**data)
        elem.notes = list(map(OutputElement.from_json, data['notes']))
        return elem


class Output(object):
    def __init__(self, errors: List[OutputElement]):
        self.errors = errors
        self.modules = {}

    @classmethod
    def from_json(cls, data: dict):
        errors = list(map(OutputElement.from_json, data['errors']))
        return cls(errors)


def parse_output(completed_process: CompletedProcess) -> Union[Output, List[str]]:
    raw_stdout = completed_process.stdout.decode('utf-8')

    try:
        data = json.loads(raw_stdout)
        output = Output.from_json(data)
        if 'modules' in data:
            output.modules = data['modules']
    except json.decoder.JSONDecodeError as e:
        return [raw_stdout, str(e)]

    output.rc = completed_process.returncode
    output.raw = raw_stdout
    return output
