import re

def read_input():
    sues = []
    with open('ex16-input.txt') as file:
        for i, line in enumerate(file):
            match = re.search('Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
            # turn alternating tuple of keys/vals into dict
            sues.append(dict(zip(match.groups()[::2], map(int, match.groups()[1::2]))))
    return sues

target_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for i, sue in enumerate(read_input()):
    if (all([target_sue[key] == sue[key] for key in sue.keys()])):
        print i + 1
