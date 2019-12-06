from time import sleep
s = 0.005
def path_a_to_b(graph, a, b, lst_a=[], i=0):
    if i >= len(graph):
        # if we are at the end of the list
        # we go back to the previous a
        print('len', len(graph), lst_a[-1])
        sleep(s)
        return path_a_to_b(graph, lst_a[-1], b, lst_a[:-1])

    # a transfer is an element of the graph
    transfer = graph[i]
    print('new path', a, b, transfer)
    if a in transfer:
        lst_a.append(a)
        if b in transfer:
            # if a and b are in the same tranfer
            # we reached our goal
            print('found b', b, transfer)
            sleep(s)
            print(lst_a)
            return len(lst_a) - 2

        # if there is only a
        # we take the other member of the transfer
        # and we look for the next one 
        print('found a', a, transfer)
        sleep(s)
        c = transfer[transfer.index(a) == 0]  # take the other object
        # no need to loop on the transfer already visited
        small_graph = list(graph)
        small_graph.remove(transfer)
        return path_a_to_b(small_graph, c, b, lst_a)  # starts back at 0

    # the a is not in the transfer
    # so we go on on the graph
    print('out', i)
    sleep(s)
    return path_a_to_b(graph, a, b, lst_a, i+1)

# get inputs
instructions = ''
with open('input2.txt', 'r') as f:
    instructions = f.read()

# construct graph
graph = []
for i in instructions.split('\n'):  # last line contains nothing
    graph.append(tuple(i.split(')')))

# path from YOU to SAN
import random
random.shuffle(graph)
result = path_a_to_b(graph, 'YOU', 'SAN')

# result
print(result)
