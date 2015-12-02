floor = 0
basement_pos = None
with open('1-input.txt') as file:
    pos = 0
    for line in file:
        for ch in line:
            if ch == '(':
                floor += 1
            elif ch == ')':
                floor -= 1

            pos += 1

            if floor < 0 and not basement_pos:
                basement_pos = pos

print basement_pos
