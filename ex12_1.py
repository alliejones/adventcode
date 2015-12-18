import json

def sum_values(tree):
    if isinstance(tree, list):
        return sum([sum_values(item) for item in tree])
    elif isinstance(tree, dict):
        if "red" in tree.values():
            return 0
        else:
            return sum([sum_values(item) for item in tree.values()])
    elif isinstance(tree, int):
        return tree
    else:
        return 0

with open('ex12-input.txt') as file:
    print sum_values(json.load(file))
