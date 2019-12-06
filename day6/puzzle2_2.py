# get inputs
instructions = ''
with open('input2.txt', 'r') as f:
    instructions = f.read()

array = instructions[:-1].split('\n')

# construct graph
graph = {}
for i in array:  # last line contains nothing
    orbited, orbiting = i.split(')')
    if orbited in graph:
        graph[orbited].add(orbiting)
    else:
        graph[orbited] = {orbiting}

    if orbiting in graph:
        graph[orbiting].add(orbited)
    else:
        graph[orbiting] = {orbited}

for k, v in graph.items():
    graph[k] = list(v)

def find_path(graph, start, end, path=None):
    if path == None:
        path = []
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            extended_path = find_path(graph, node, end, path)
            if extended_path:
                return extended_path
    return None

# path from YOU to SAN
#result = path_a_to_b(graph, 'YOU', 'SAN')
path = find_path(graph, 'YOU', 'SAN')

# result
result = len(path) - 2
print(result)
