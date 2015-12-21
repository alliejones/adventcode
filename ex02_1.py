total_area = 0

with open('ex02-input.txt') as file:
    for line in file:
        sides = map(int, line.split('x'))
        w, h, l = sides
        area = 2*l*w + 2*w*h + 2*h*l

        sides.remove(max(*sides))
        area += sides[0] * sides[1]
        total_area += area

print total_area
