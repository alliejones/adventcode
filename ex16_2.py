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

def matches_target_sue(sue):
    for key in sue.keys():
        if key in ('cats', 'trees'):
            if sue[key] <= target_sue[key]:
                return False
        elif key in ('pomeranians', 'goldfish'):
            if sue[key] >= target_sue[key]:
                return False
        else:
            if sue[key] != target_sue[key]:
                return False

    return True

for i, sue in enumerate(read_input()):
    if matches_target_sue(sue):
        print i + 1
