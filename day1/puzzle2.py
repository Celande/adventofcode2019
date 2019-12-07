import math

def get_fuel_from_mass(mass):
    return math.floor((mass / 3)) - 2

a = []
with open('input2.txt', 'r') as fl:
    l = fl.readline()
    while l:
        try:
            l = float(l)
            f = get_fuel_from_mass(l)
            s = f
            while f > 0:
                f = get_fuel_from_mass(f)
                if f <= 0:
                    break
                s += f
            a.append(s)
        except ValueError:
            pass
        l = fl.readline()

s = sum(int(i) for i in a )

print(s)
