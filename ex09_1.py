import re
import itertools

distances = {}
with open('ex09-input.txt') as file:
    for line in file:
        c1, c2, dist = re.search('(\w+) to (\w+) = (\d+)', line).groups()

        if not c1 in distances:
            distances[c1] = {}
        distances[c1][c2] = int(dist)

        if not c2 in distances:
            distances[c2] = {}
        distances[c2][c1] = int(dist)

paths = itertools.permutations(distances.keys())
path_distances = {}
for path in paths:
    dist = 0
    for i, city in enumerate(path):
        if i < len(path) - 1:
            next_city = path[i+1]
            dist += distances[city][next_city]
    path_distances[path] = dist

print min(path_distances.values())

# part 2
print max(path_distances.values())
