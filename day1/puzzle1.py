import math
a = []
with open('input.txt', 'r') as f:
    l = f.readline()
    while l:
        try:
            l = float(l)
            a.append(math.floor(l/3)-2)
        except ValueError:
            pass
        l = f.readline()

print(sum(int(i) for i in a ))
