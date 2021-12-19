from linereader import read_file

d = [x for x in read_file('12.in.txt')]


def create_graph(lines):
    pairs = [tuple(line.split('-')) for line in lines]

    verticies = list(set([node for tup in pairs for node in tup]))
    graph = dict().fromkeys(verticies, [])

    for src, dest in pairs:
        if dest not in graph[src] and dest != 'start':
            graph[src] = [*graph[src], dest]
        if src not in graph[dest] and src != 'start':
            graph[dest] = [*graph[dest], src]

    return graph


def find_paths(graph, vertex, visited, flag=False):
    visited.append(vertex)
    if vertex == 'end':
        return [visited]

    paths = []
    for neighbour in graph[vertex]:
        if neighbour not in visited or neighbour.isupper():
            new_paths = find_paths(graph, neighbour, visited.copy(), flag)
            paths.extend(new_paths)
        elif neighbour.islower() and flag:

            new_paths = find_paths(graph, neighbour, visited.copy(), False)
            paths.extend(new_paths)
    return paths


g = create_graph(d)

p = find_paths(g, 'start', [], False)
print("p1:", len(p))

p = find_paths(g, 'start', [], True)
print("p2:", len(p))
