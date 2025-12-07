
def parse(f):
    rotations = []
    for line in f:
        sign = -1 if line[0] == 'L' else 1
        rotations.append(sign * int(line[1:]))
    return rotations

def part1(rotations):
    n = 50
    count = 0
    for r in rotations:
        n = (n + r) % 100
        if n == 0:
            count += 1
    return count

def part2(rotations):
    n = 50
    count = 0
    for r in rotations:
        d = r / abs(r)
        for _ in range(abs(r)):
            n = (n + d) % 100
            if n == 0:
                count += 1
    return count

with open("../input/day1.txt") as f:
    rotations = parse(f)
    print(part1(rotations))
    print(part2(rotations))