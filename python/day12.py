
def solve(lines):
    total = 0
    for line in lines:
        tokens = line.split()
        if len(tokens) > 1:
            area = tokens[0][:-1].split('x')
            width = int(area[0])
            height = int(area[1])
            tile_count = sum(map(int, tokens[1:]))
            if tile_count * 9 <= width * height:
                total += 1
    return total

with open("../input/day12.txt") as f:
    print(solve(f.readlines()))
