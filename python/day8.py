import math

def parse(f):
    return [tuple(map(int, line.strip().split(','))) for line in f]

def distance_squared(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    c = p2[2] - p1[2]
    return a * a + b * b + c * c

def calc_distances(points):
    num_points = len(points)
    distances = []
    for a in range(num_points):
        for b in range(a + 1, num_points):
            d = distance_squared(points[a], points[b])
            distances.append((d, a, b))
    return sorted(distances)

def get_circuit_size(p, cmap, visited):
    if visited[p]:
        return 0

    visited[p] = True
    total = 1
    for link in cmap[p]:
        total += get_circuit_size(link, cmap, visited)
    return total

def build_cmap(distances, num_points, num_links):
    cmap = [[] for _ in range(num_points)]
    for (d, a, b) in distances[:num_links]:
        cmap[a].append(b)
        cmap[b].append(a)
    return cmap


def part1(points):
    num_points = len(points)
    distances = calc_distances(points)
    # In test mode, take the first 10 links.
    # Otherwise, take the first 1000.
    num_links = 1000 if num_points == 1000 else 10
    cmap = build_cmap(distances, num_points, num_links)
    visited = [False for _ in range(num_points)]
    sizes = []
    for p in range(num_points):
        n = get_circuit_size(p, cmap, visited)
        if n > 0:
            sizes.append(n)
    sizes.sort(reverse=True)
    return math.prod(sizes[:3])

def part2(points):
    num_points = len(points)
    distances = calc_distances(points)
    # Could speed this up with a binary search but it's good enough
    for i in range(1, len(distances)):
        cmap = build_cmap(distances, num_points, i)
        visited = [False for _ in range(num_points)]
        if get_circuit_size(0, cmap, visited) == num_points:
            (_, a, b) = distances[i-1]
            return points[a][0] * points[b][0]
    return 0

with open("../input/day8.txt") as f:
    points = parse(f)
    print(part1(points))
    print(part2(points))
