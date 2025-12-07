
def parse(f):
    return [list(line.strip()) for line in f]

def get_cell(grid, x, y):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return grid[y][x]
    else:
        return None

def coords(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield x, y

def neighbours(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                yield x + dx, y + dy

def count_rolls(grid, x, y):
    return [get_cell(grid, x, y) for x, y in neighbours(x, y)].count('@')

def part1(grid):
    n = 0
    for x, y in coords(grid):
        if get_cell(grid, x, y) == '@' and count_rolls(grid, x, y) < 4:
            n += 1
    return n

def part2(grid):
    g = [row[:] for row in grid] # Copy the grid
    n = 0
    done = False
    while not done:
        done = True
        for x,y in coords(g):
            if get_cell(g, x, y) == '@' and count_rolls(g, x, y) < 4:
                g[y][x] = '.'
                n += 1
                done = False
    return n

with open("../input/day4.txt") as f:
    grid = parse(f)
    print(part1(grid))
    print(part2(grid))
