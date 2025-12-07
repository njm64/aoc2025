
def parse(f):
    ranges = []
    for t in "".join(f.readlines()).split(","):
        ranges.append(tuple(t.split("-")))
    return ranges

def process_range(r, part):
    (a, b) = r
    values = set()
    r = range(int(r[0]), int(r[1]) + 1)
    max_pattern_len = len(b) // 2
    for pattern_len in range(1, max_pattern_len + 1):
        for value_len in range(len(a), len(b) + 1):
            if value_len != pattern_len and value_len % pattern_len == 0:
                pattern_count = value_len // pattern_len
                if part == 2 or pattern_count == 2:
                    min_pattern = pow(10, pattern_len - 1)
                    max_pattern = pow(10, pattern_len) - 1
                    for pattern in range(min_pattern, max_pattern + 1):
                        value = int(str(pattern) * pattern_count)
                        if value in r:
                            values.add(value)
    return sum(values)

def part1(rs):
    return sum([process_range(r, 1) for r in rs])

def part2(rs):
    return sum([process_range(r, 2) for r in rs])

with open("../input/day2.txt") as f:
    ranges = parse(f)
    print(part1(ranges))
    print(part2(ranges))

