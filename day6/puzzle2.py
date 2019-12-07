def path_a_to_b(graph, start, end, n_orbits=0):
    for orbit in graph.get(start, []):
        if orbit == end:
            return n_orbits - 1

        following = path_a_to_b(
            {k: v for k, v in graph.items() if k != start},  # removes already used key/value
            orbit, end, n_orbits + 1
        )

        if following:
            return following

    # returns None by default

# get inputs
instructions = ''
with open('input2.txt', 'r') as f:
    instructions = f.read()

array = instructions[:-1].split('\n')  # last line contains nothing

# construct graph
graph = {}
# creating all the bidirectionnal links
for i in array:
    # using set to avoid duplicates
    orbited, orbiting = i.split(')')
    if orbited in graph:
        graph[orbited].add(orbiting)
    else:
        graph[orbited] = {orbiting}

    if orbiting in graph:
        graph[orbiting].add(orbited)
    else:
        graph[orbiting] = {orbited}

# result
result = path_a_to_b(graph, 'YOU', 'SAN')
print(result)
