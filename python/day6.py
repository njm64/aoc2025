import math
import itertools

def transpose(values):
    return list(map(list, itertools.zip_longest(*values, fillvalue=' ')))

def part1(input):
    rows = transpose([line.split() for line in input])
    total = 0
    for row in rows:
        op = row[-1]
        values = map(int, row[:-1])
        if op == '+':
            total += sum(values)
        elif op == '*':
            total += math.prod(values)
    return total

def part2(input):
    data = transpose(input)
    total = 0
    acc = 0
    op = ""
    for row in data:
        val = "".join(row[:-1]).strip()
        if len(val) == 0:
            continue
        if row[-1] != ' ':
            total += acc
            acc = int(val)
            op = row[-1]
        elif op == "*":
            acc *= int(val)
        elif op == "+":
            acc += int(val)
    total += acc
    return total

with open("../input/day6.txt") as f:
    input = f.readlines()
    print(part1(input))
    print(part2(input))
