def manhattan_dist(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def intersection(d1, d2):
    result = []
    for k, v in d1.items():
        a = d2.get(k, None)
        if a:
            result.append(Coord(k[0], k[1], v+a))
    return result

class Coord():
    def __init__(self, x, y, steps=0):
        self.x = x
        self.y = y
        self.steps = steps

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y, self.steps))

    def __repr__(self):
        return '(%s, %s | %s)' % (self.x, self.y, self.steps)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('lel')
        return (self.x, self.y)[key]

    def move(self, go):
        old_x, old_y, old_steps = self.x, self.y, self.steps
        direction = go[0]
        step = int(go[1:])

        # return every points crossed
        if direction == 'U':  # up
            self.y += step
            self.steps += step
            return [Coord(self.x, i, old_steps+e+1) for e, i in enumerate(range(old_y+1, self.y+1))]
        if direction == 'D':  # down
            self.y -= step
            self.steps += step
            return [Coord(self.x, i, old_steps+e+1) for e, i in enumerate(range(old_y-1, self.y-1, -1))]
        if direction == 'L':  # left
            self.x -= step
            self.steps += step
            return [Coord(i, self.y, old_steps+e+1) for e, i in enumerate(range(old_x-1, self.x-1, -1))]
        if direction == 'R':  # right
            self.x += step
            self.steps += step
            return [Coord(i, self.y, old_steps+e+1) for e, i in enumerate(range(old_x+1, self.x+1))]

    def path(self, instructions):
        points = []
        for i in instructions:
            m = self.move(i)
            points += m
        return points

# get inputs
wires = {}
with open('input2.txt', 'r') as f:
    line = f.readline()
    i = 1
    while line:
        wires[i] = line.replace('\n', '').split(',')
        line = f.readline()
        i += 1

# get paths
# as dict to be compared faster
for k, v in wires.items():
    wires[k] = {(c.x, c.y): c.steps for c in Coord(0, 0).path(v)}

# get intersections
intersec = []
for k1, v1 in wires.items():
    intersec += [intersection(v1, v2) for k2, v2 in wires.items() if k1 != k2][0]

intersec = list(intersec)

# get intersection with less steps
print(min(intersec, key=lambda x: x.steps).steps)
