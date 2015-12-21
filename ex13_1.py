import re
from itertools import permutations

def read_happiness_vals():
    vals = {}
    with open('ex13-input.txt') as file:
        for line in file:
            matches = re.finditer('(\w+) would (gain|lose) (\d+) .* (\w+)\.$', line)
            for match in matches:
                p1, gain_lose, amt, p2 = match.groups()

                if not p1 in vals:
                    vals[p1] = {}

                amt = int(amt)
                if gain_lose == 'lose':
                    amt = amt * -1

                vals[p1][p2] = amt
    return vals

def calc_happiness_totals(happiness_vals):
    happiness_totals = []
    perms = permutations(happiness_vals.keys())

    for arrangement in perms:
        total = 0
        for i, p1 in enumerate(arrangement):
            p2 = arrangement[i-1]
            total += happiness_vals[p1][p2]
            total += happiness_vals[p2][p1]
        happiness_totals.append(total)

    return happiness_totals

vals = calc_happiness_totals(read_happiness_vals())
print max(vals)
