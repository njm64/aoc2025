

def parse(lines):
    g = {}
    for line in lines:
        key, rhs = line.split(": ")
        g[key] = rhs.split()
    return g

def sort_graph(graph, src):
    visited = set()
    nodes = []
    def visit(node):
        if node in visited:
            return
        for link in graph.get(node, []):
            visit(link)
        visited.add(node)
        nodes.append(node)

    visit(src)
    nodes.reverse()
    return nodes

def invert_graph(graph):
    inverted = {}
    for node, links in graph.items():
        for link in links:
            if not link in inverted:
                inverted[link] = [node]
            else:
                inverted[link].append(node)
    return inverted

def count_paths(graph, src, dst):
    nodes = sort_graph(graph, src)
    src_map = invert_graph(graph)
    count_map = {src : 1}
    for node in nodes[1:]:
        count = 0
        for src in src_map[node]:
            count += count_map.get(src, 0)
        count_map[node] = count
    return count_map[dst]

def part1(graph):
    return count_paths(graph, "you", "out")

def part2(graph):
    return \
        count_paths(graph, "svr", "fft") * \
        count_paths(graph, "fft", "dac") * \
        count_paths(graph, "dac", "out")

with open("../input/day11.txt") as f:
    graph = parse(f)
    print(part1(graph))
    print(part2(graph))
