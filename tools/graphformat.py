#!/usr/bin/env python3
# Parse and format the typegraph which can be produced by using the '--mi --dump-typegraph' flags
# That graph is in json. This Script takes said json and prints the graph in graphviz format
# dependencies: graphviz

import json
import sys

from graphviz import Digraph


def main():
    compiler_output = sys.stdin.read()
    parsed = None

    try:
        parsed = json.loads(compiler_output)
    except json.JSONDecodeError:
        print('Could not parse json')
        exit(-1)

    if 'type-graph' not in parsed:
        print("No type-graph in compiler output")
        exit(-2)

    tg = parsed['type-graph']
    if 'name' not in tg or 'nodes' not in tg:
        print("type-graph has invalid format")
        exit(-3)

    dot = Digraph(tg['name'])
    for n in tg['nodes']:
        dot.node(n['ty'])
        # handling the outs is enough
        for o in n['out']:
            style = 'dotted' if o['kind'] == 'soft' else ''
            dot.edge(n['ty'], o['ty'], style=style)

    print(dot.source)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('graphformat')
        print('Felix Schoeller <felix.schoeller@protonmail.com>')
        print('Convert the json formatted output of the kantan compiler into the graphviz format')
        print('\nUSAGE:')
        print(f'    kantan myfile.kan --mi --dump-type-graph | {sys.argv[0]} | dot -Tpng > myfile.png')
        exit(0)

    main()
