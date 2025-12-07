
def parse_range(s):
    return list(map(int, s.split('-')))

def parse(f):
    lines = [line.strip() for line in f]
    blank_index = lines.index("")
    ranges = list(map(parse_range, lines[:blank_index]))
    ingredients = list(map(int, lines[blank_index + 1:]))
    return sorted(ranges), ingredients

def check_fresh(ranges, ingredient):
    for (start, end) in ranges:
        if start <= ingredient <= end:
            return True
    return False

def part1(ranges, ingredients):
    n = 0
    for ingredient in ingredients:
        if check_fresh(ranges, ingredient):
            n += 1
    return n

def part2(ranges):
    prev_end = 0
    total = 0
    for (start, end) in ranges:
        if start > prev_end:
            # No overlap
            total += (end - start) + 1
            prev_end = end
        elif end > prev_end:
            # Partial Overlap
            total += (end - prev_end)
            prev_end = end
    return total

with open("../input/day5.txt") as f:
    ranges, ingredients = parse(f)
    print(part1(ranges, ingredients))
    print(part2(ranges))




