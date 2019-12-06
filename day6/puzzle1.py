def get_list_indirect(graph, orbited, lst):
    # modifying a list
    # so no need to return anything
    for orbiting in graph.get(orbited, []):
        # hoping for no cicles
        lst.append(orbiting)
        get_list_indirect(graph, orbiting, lst)

# get inputs
instructions = ''
with open('input1.txt', 'r') as f:
    instructions = f.read()

# construct graph
graph = {}
for i in instructions[:-1].split('\n'):  # last line contains nothing
    orbited, orbiting = i.split(')')
    if orbited in graph:
        graph[orbited].append(orbiting)
    else:
        graph[orbited] = [orbiting]

# visualising graph
# for k, v in graph.items():
#     print('%s: %s' % (k, v))

# direct and indirect orbit
list_indirect_orbits = []
for orbited in graph.keys():
    lst = []
    get_list_indirect(graph, orbited, lst)
    list_indirect_orbits.append(lst)

# result
result = sum(len(o) for o in list_indirect_orbits)
print(result)
