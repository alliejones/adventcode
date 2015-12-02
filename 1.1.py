floor = 0
with open('1-input.txt') as file:
    for line in file:
        for ch in line:
            if ch == '(':
                floor += 1
            elif ch == ')':
                floor -= 1
print floor
