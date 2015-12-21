total_length = 0

with open('ex02-input.txt') as file:
    for line in file:
        sides = map(int, line.split('x'))
        w, h, l = sides

        volume = w * h *l
        total_length += volume

        sides.remove(max(*sides))
        total_length += sides[0]*2 + sides[1]*2

print total_length
