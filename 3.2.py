santa_pos = (0,0)
robo_pos = (0,0)
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

with open('3-input.txt') as file:
    turn = 'santa'
    for line in file:
        for c in line:
            if (turn == 'santa')
                new_pos = santa_pos = update_pos(santa_pos, c)
                turn = 'robo'
            else:
                new_pos = robo_pos = update_pos(robo_pos, c)
                turn = 'santa'

            if pos not in presents:
                presents[pos] = 1
            else:
                presents[pos] += 1

print len(presents)
