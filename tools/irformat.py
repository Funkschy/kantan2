#!/usr/bin/env python3
# Parse and format the ir which can be produced by using the '--mi --dump-ir' flags
# That ir is in json. This Script takes said json and prints the human readable ir format

import json
import sys


def main():
    compiler_output = sys.stdin.read()
    parsed = None

    try:
        parsed = json.loads(compiler_output)
    except json.JSONDecodeError:
        print('Could not parse json')
        exit(-1)

    if 'ir' not in parsed:
        print("No ir in compiler output")
        exit(-2)

    modules = parsed['ir']
    for mod in modules:
        if 'path' not in mod or 'functions' not in mod:
            print('ir has invalid format')
            exit(-3)

        print(mod['path'])
        for function in mod['functions']:
            print('    def', function['original_name'], '() {')

            for local in function['locals']:
                print('        let', local['name'], ':', local['type'])

            for bb_name in function['blocks']:
                bb = function['blocks'][bb_name]
                print('       ', bb_name, '{')

                for stmt in bb['statements']:
                    if stmt['kind'] == 'assignment':
                        print_location(stmt['location'])
                        print(' =', end='')
                        print_value(stmt['value'], indent=0)
                        print()

                print_terminator(bb['terminator'])
                print()
                print('        }')

            print('    }')


def print_location(location, indent=12):
    string = ''

    if location['kind'] == 'local':
        string = location['name']
    else:
        assert False, location['kind']

    projs = location['projections']
    for p in projs:
        if p['kind'] == 'deref':
            string = f'(*{string})'

    print(' ' * max(0, indent - 1), string, end='')


def print_value(value, indent=12):
    if value['kind'] == 'use':
        print_operand(value['operand'], indent)
    elif value['kind'] == 'ref':
        print(' ' * max(0, indent - 1), '&', end='')
        print_location(value['location'], indent=0)
    elif value['kind'] == 'unary':
        print(' ' * max(0, indent - 1), value['unary-kind'], end='')
        print('(', end='')
        print_operand(value['operand'], indent=0)
        print(')', end='')
    elif value['kind'] == 'binary':
        print_operand(value['left'], indent)
        print('', value['binary-kind'], end='')
        print_operand(value['right'], indent=0)
    else:
        assert False, value['kind']


def print_operand(operand, indent=12):
    if operand['kind'] == 'constant':
        print_const(operand['value'], indent)
    elif operand['kind'] == 'copy':
        print_location(operand['location'], indent)
    else:
        assert False, operand['kind']


def print_const(const, indent=12):
    if const is None:
        pass
    elif const['kind'] == 'undefined':
        print(' ' * (indent - 1), 'undefined', end='')
    elif const['kind'] == 'null':
        print(' ' * (indent - 1), 'null', end='')
    elif const['kind'] in ('int', 'float', 'char'):
        print(' ' * (indent - 1), const['value'], end='')
    elif const['kind'] == 'string':
        print(' ' * (indent - 1), '"' + const['value'] + '"', end='')
    elif const['kind'] == 'function':
        print(' ' * (indent - 1), const['name'], end='')
    else:
        assert False, const['kind']


def print_terminator(terminator, indent=12):
    if terminator['kind'] == 'nop':
        print(' ' * (indent - 1), 'nop', end='')
    elif terminator['kind'] == 'return':
        print(' ' * (indent - 1), 'return', end='')
        print_operand(terminator['operand'], indent=0)
    elif terminator['kind'] == 'call':
        print_location(terminator['dest'], indent)
        print(' =', 'call', end='')
        print_operand(terminator['callee'], indent=0)
        print(' ->', terminator['next'], end='')
    else:
        assert False, terminator['kind']


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('irformat')
        print('Felix Schoeller <felix.schoeller@protonmail.com>')
        print('Convert the json formatted ir output of the kantan compiler into a human readable format')
        print('\nUSAGE:')
        print(f'    kantan myfile.kan --mi --dump-ir | {sys.argv[0]}')
        exit(0)

    main()
