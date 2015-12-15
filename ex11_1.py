import re
from string import ascii_lowercase

def uses_valid_letters(pw):
    return re.search('(i|o|l)', pw) == None

def invalid_letter_indexes(pw):
    return [m.start(0) for m in re.finditer('(i|o|l)', pw)]

def letter_pair_count(pw):
    prev_c = None
    pair_count = 0
    for c in pw:
        if c == prev_c:
            pair_count += 1
            prev_c = None
        else:
            prev_c = c
    return pair_count

def has_letter_straight(pw):
    return any([is_triple_consecutive(t) for t in get_letter_triples(pw)])

def get_letter_triples(pw):
    return zip(pw, pw[1:], pw[2:])

def is_triple_consecutive(triple):
    a, b, c = [ord(x) for x in triple]
    return b - a == 1 and c - b == 1

def is_valid_password(pw):
    return (uses_valid_letters(pw) and
            letter_pair_count(pw) > 1 and
            has_letter_straight(pw))

# we can treat these strings as base-26 values
def password_int_value(pw):
    offset = ord('a')
    chars = list(pw)
    chars.reverse()
    return sum([(ord(c) - offset) * (26**i) for i, c in enumerate(chars)])

def get_pw_from_int_value(int_val, pw_len=8):
    chars = []
    for i in range(pw_len):
        int_val, c = divmod(int_val, 26)
        chars.insert(0, ascii_lowercase[c])
    return ''.join(chars)

def next_char_seq(s):
    return get_pw_from_int_value(password_int_value(s) + 1)

def get_next_pw(pw):
    next_pw = next_char_seq(pw)
    while not is_valid_password(next_pw):
        next_pw = next_char_seq(next_pw)

    return next_pw
