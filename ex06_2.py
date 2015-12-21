import re

size = 1000

grid = [[0 for x in range(size)] for y in range(size)]

def print_grid(grid):
    for row in grid:
        print ''.join(map(str, row))

def new_value(op, curr_val):
    if op == 'turn on':
        return curr_val + 1
    elif op == 'turn off':
        return max(0, curr_val - 1)
    elif op == 'toggle':
        return curr_val + 2

def update_grid(grid, op, tl_x, tl_y, br_x, br_y):
    for row in range(tl_y, br_y+1):
        for col in range(tl_x, br_x+1):
            grid[row][col] = new_value(op, grid[row][col])

def total_brightness(grid):
    brightness = 0
    for row in grid:
        for light in row:
            brightness += light
    return brightness

def parse_instr(str):
    matches = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', str)
    coords = map(int, matches.groups()[1:])
    return [matches.group(1)] + coords

def process_line(line):
    update_grid(grid, *parse_instr(line))

if __name__ == '__main__':
    with open('ex06-input.txt') as file:
        for line in file:
            process_line(line)

    print total_brightness(grid)
