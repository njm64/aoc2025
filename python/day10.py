from itertools import combinations
from functools import reduce
from operator import xor

def parse_lights(s):
    n = 0
    for c in reversed(s[1:-1]):
        n = n << 1
        if c == '#':
            n = n | 1
    return n

def parse_int_list(s):
    return [int(i) for i in s[1:-1].split(',')]

def parse_button(s):
    return reduce(lambda b, i: b | (1 << i), parse_int_list(s), 0)

def parse_machine(line):
    tokens = line.split()
    lights = parse_lights(tokens[0])
    buttons = [parse_button(t) for t in tokens[1:-1]]
    joltages = parse_int_list(tokens[-1])
    return lights, buttons, joltages

def parse(lines):
    return [parse_machine(line) for line in lines]

def find_combinations(buttons, mask):
    for i in range(len(buttons) + 1):
        for bs in combinations(buttons, i):
            if reduce(xor, bs, mask) == 0:
                yield bs

def solve_part1(machine):
    (lights, buttons, _) = machine
    return len(next(find_combinations(buttons, lights)))

# Based on this clever approach:
# https://old.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
def solve_part2(machine):
    (_, buttons, joltages) = machine
    cache = {}
    def step(joltages):
        if all(j == 0 for j in joltages):
            return 0
        key = str(joltages)
        if key in cache:
            return cache[key]
        best = None
        mask = reduce(lambda m, j: (m << 1) | (j % 2), reversed(joltages), 0)
        for bs in find_combinations(buttons, mask):
            new_joltages = list(joltages)
            for b in bs:
                for j in range(len(joltages)):
                    if b & (1 << j):
                        new_joltages[j] -= 1
            if all(j >= 0 for j in new_joltages):
                n = step([j // 2 for j in new_joltages])
                if n is not None:
                    n = n * 2 + len(bs)
                    if best is None or n < best:
                        best = n
        cache[key] = best
        return best
    return step(joltages)

def part1(machines):
    return sum(map(solve_part1, machines))

def part2(machines):
    return sum(map(solve_part2, machines))

with open("../input/day10.txt") as f:
    machines = parse(f)
    print(part1(machines))
    print(part2(machines))

