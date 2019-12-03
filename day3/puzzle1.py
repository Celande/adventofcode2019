def manhattan_dist(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('lel')
        return (self.x, self.y)[key]

    def move(self, go):
        old_x, old_y = self.x, self.y
        direction = go[0]
        step = int(go[1:])

        # return every points crossed
        if direction == 'U':  # up
            self.y += step
            return [Coord(self.x, i) for i in range(old_y+1, self.y+1)]
        if direction == 'D':  # down
            self.y -= step
            return [Coord(self.x, i) for i in range(self.y+1, old_y+1)]
        if direction == 'L':  # left
            self.x -= step
            return [Coord(i, self.y) for i in range(self.x+1, old_x+1)]
        if direction == 'R':  # right
            self.x += step
            return [Coord(i, self.y) for i in range(old_x+1, self.x+1)]

    def path(self, instructions):
        points = []
        for i in instructions:
            points += self.move(i)
        return set(points)  # no duplicate

# get inputs
wires = {}
with open('input1.txt', 'r') as f:
    line = f.readline()
    i = 1
    while line:
        wires[i] = line.replace('\n', '').split(',')
        line = f.readline()
        i += 1

# get paths
for k, v in wires.items():
    wires[k] = set(Coord(0, 0).path(v))

# get intersections
intersec = set()
for k1, v1 in wires.items():
    intersec = intersec.union(v1.intersection(*[v2 for k2, v2 in wires.items() if k1 != k2]))

intersec = list(intersec)

# get closest intersection
distances = [manhattan_dist((0,0), i) for i in intersec]
print(min(distances))
