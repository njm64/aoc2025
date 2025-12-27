
def parse(f):
    return [tuple(map(int, line.strip().split(','))) for line in f]

def part1(points):
    max_area = 0
    for i, (x1,y1) in enumerate(points):
        for (x2,y2) in points[i+1:]:
            dx = abs(x2 - x1) + 1
            dy = abs(y2 - y1) + 1
            area = dx * dy
            if area > max_area:
                max_area = area
    return max_area

def find_point_in_rect(points, min_x, min_y, max_x, max_y):
    for (x, y) in points:
        if min_x < x < max_x and min_y < y < max_y:
            return True
    return False

def find_upper_rect(points, p):
    (max_x, max_y) = p
    max_area = 0
    rect = None
    for (min_x, min_y) in points:
        if min_y >= max_y or min_x >= max_x:
            continue
        if find_point_in_rect(points, min_x, min_y, max_x, max_y):
            continue
        dx = max_x - min_x + 1
        dy = max_y - min_y + 1
        area = dx * dy
        if area > max_area:
            max_area = area
            rect = (min_x, min_y, dx, dy)
    return (max_area, rect)

def find_lower_rect(points, p):
    (max_x, min_y) = p
    max_area = 0
    rect = None
    for (min_x, max_y) in points:
        if min_y >= max_y or min_x >= max_x:
            continue
        if find_point_in_rect(points, min_x, min_y, max_x, max_y):
            continue
        dx = max_x - min_x + 1
        dy = max_y - min_y + 1
        area = dx * dy
        if area > max_area:
            max_area = area
            rect = (min_x, min_y, dx, dy)
    return (max_area, rect)

def render(points, r):
    (x, y, w, h) = r
    with open("shape.svg", "w") as f:
        f.write("<svg width='100000' height='100000'>\n")
        prev = points[-1]
        for p in points:
            f.write(f'<line x1="{prev[0]}" y1="{prev[1]}" x2="{p[0]}" y2="{p[1]}" stroke="black" stroke-width="20"/>\n')
            prev = p
        f.write(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="red" stroke-width="20" fill="none"/>\n')
        f.write('</svg>\n')

def part2(points):
    # After rendering the shape to SVG, it becomes apparent that it's approximately a
    # circle, split in the middle by two horizontal lines, and that the largest rectangle
    # must share a vertex with one of these horizontal lines.
    a1, r1 = find_upper_rect(points, (94891, 48378))
    a2, r2 = find_lower_rect(points, (94891, 50375))
    #render(points, r2)
    return max(a1, a2)

with open("../input/day9.txt") as f:
    points = parse(f)
    print(part1(points))
    print(part2(points))
