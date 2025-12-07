
def parse(f):
    return [list(map(int, line.strip())) for line in f]

def max_joltage(bank, batteries):
    j = 0
    remaining = batteries
    while remaining > 0:
        remaining -= 1
        d = max(bank[:len(bank)-remaining])
        i = bank.index(d)
        j = j * 10 + d
        bank = bank[i+1:]
    return j

def part1(batteries):
    return sum(map(lambda b: max_joltage(b, 2), batteries))

def part2(batteries):
    return sum(map(lambda b: max_joltage(b, 12), batteries))

with open("../input/day3.txt") as f:
    banks = parse(f)
    print(part1(banks))
    print(part2(banks))