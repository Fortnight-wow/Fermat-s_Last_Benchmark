import csv
from pathlib import Path


RESULTS_FILE = Path('leaderboard/results_template.csv')


def load_results():
    with open(RESULTS_FILE, newline='') as file:
        return list(csv.DictReader(file))


if __name__ == '__main__':
    results = load_results()
    print(f'Loaded {len(results)} benchmark entries.')
