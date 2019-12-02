l = ''
with open('input1.txt', 'r') as f:
    l = f.read()

a = [int(e) for e in l.split(',')]
# instructions
a[1] = 12
a[2] = 2

i = 0
opcode = 0
input_1 = 1
input_2 = 2
output = 3
while i < len(a):
    if a[i] == 99:
        break
    opcode_set = a[i:i + 4]
    if opcode_set[opcode] == 1:
        a[opcode_set[output]] = a[opcode_set[input_1]] + a[opcode_set[input_2]]
    else:  # == 2
        a[opcode_set[output]] = a[opcode_set[input_1]] * a[opcode_set[input_2]]
    i += 4

print(a[0])
