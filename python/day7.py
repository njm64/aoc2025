
def part1(rows):
    beams = set()
    beams.add(rows[0].index('S'))
    splits = 0
    for row in rows[1:]:
        new_beams = set()
        for beam in beams:
            if row[beam] == '^':
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                splits += 1
            else:
                new_beams.add(beam)
            beams = new_beams
    return splits

def part2(rows):
    beams = {rows[0].index('S') : 1}
    for row in rows[1:]:
        new_beams = {}
        for (beam, count) in beams.items():
            if row[beam] == '^':
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + count
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + count
            else:
                new_beams[beam] = new_beams.get(beam, 0) + count
        beams = new_beams
    return sum(beams.values())

with open("../input/day7.txt") as f:
    rows = [line.strip() for line in f]
    print(part1(rows))
    print(part2(rows))
