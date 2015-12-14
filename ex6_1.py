import re

SIZE = 1000

grid = [[0 for x in range(SIZE)] for y in range(SIZE)]

def print_grid(grid):
    for row in grid:
        print ''.join(map(str, row))

def new_value(op, curr_val):
    if op == 'turn on':
        return 1
    elif op == 'turn off':
        return 0
    elif op == 'toggle':
        if curr_val == 1:
            return 0
        else:
            return 1

def update_grid(grid, op, tl_x, tl_y, br_x, br_y):
    for row in range(tl_y, br_y+1):
        for col in range(tl_x, br_x+1):
            grid[row][col] = new_value(op, grid[row][col])

def lit_count(grid):
    count = 0
    for row in grid:
        for light in row:
            if light == 1:
                count += 1
    return count

def parse_instr(str):
    matches = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', str)
    coords = map(int, matches.groups()[1:])
    return [matches.group(1)] + coords

def process_line(line):
    update_grid(grid, *parse_instr(line))

if __name__ == '__main__':
    with open('6-input.txt') as file:
        for line in file:
            process_line(line)

    print lit_count(grid)
