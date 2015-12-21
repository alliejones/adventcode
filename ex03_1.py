pos = (0,0)
presents = {}

def update_pos(pos, c):
    if c == '^':
        new_pos = (pos[0], pos[1] + 1)
    elif c == '<':
        new_pos = (pos[0] - 1, pos[1])
    elif c == 'v':
        new_pos = (pos[0], pos[1] - 1)
    elif c == '>':
        new_pos = (pos[0] + 1, pos[1])

    return new_pos

with open('ex03-input.txt') as file:
    for line in file:
        for c in line:
            pos = update_pos(pos, c)

            if pos not in presents:
                presents[pos] = 1
            else:
                presents[pos] += 1

print len(presents)
