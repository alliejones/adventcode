import re

good_strings = []

def is_good(str):
    has_three_vowels = len(re.sub(r'[^aeiou]', '', str)) >= 3
    has_dup_char = re.search(r'(\w)\1', str) != None
    no_disallowed_str = re.search(r'(ab|cd|pq|xy)', str) == None

    return has_three_vowels and has_dup_char and no_disallowed_str

with open('ex05-input.txt') as file:
    for line in file:
        if is_good(line):
            good_strings.append(line)

print(len(good_strings))
