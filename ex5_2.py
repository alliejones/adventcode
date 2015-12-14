import re

good_strings = []

def has_repeated_pair(str):
    found = False
    for i, c in enumerate(str):
        if i > len(str) - 2:
            return

        pair = c + str[i+1]
        if pair in str[i+2:]:
            found = True
            break
    return found

# repeated with one char between
def has_repeated_char(str):
    found = False
    for i, c in enumerate(str):
        if i > len(str) - 3:
            return

        if c == str[i+2]:
            found = True
            break
    return found

def is_good(str):
    return has_repeated_pair(str) and has_repeated_char(str)

with open('5-input.txt') as file:
    for line in file:
        if is_good(line):
            good_strings.append(line)

print(len(good_strings))
