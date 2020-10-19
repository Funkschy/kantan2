import json
from subprocess import CompletedProcess
from typing import List


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

    @classmethod
    def from_json(cls, data: dict):
        errors = list(map(OutputElement.from_json, data['errors']))
        return cls(errors)


def parse_output(completed_process: CompletedProcess) -> Output:
    raw_stdout = completed_process.stdout.decode('utf-8')
    output = Output.from_json(json.loads(raw_stdout))
    output.rc = completed_process.returncode
    output.raw = raw_stdout
    return output
