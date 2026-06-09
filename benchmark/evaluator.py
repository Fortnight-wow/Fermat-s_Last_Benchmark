"""
Simple benchmark evaluator.

First version written for the Fermat's Last Benchmark project.
"""

import json


def load_problem(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    print('Evaluator initialized.')