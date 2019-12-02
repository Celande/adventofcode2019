l = ''
with open('input2.txt', 'r') as f:
    l = f.read()

a = [int(e) for e in l.split(',')]
reset = list(a)
# instructions
opcode = 0
input_1 = 1
input_2 = 2
output = 3

for noun in range(1, 100):
    for verb in range(1, 100):
        a = list(reset)
        a[1] = noun
        a[2] = verb

        for i in range(0, len(a), 4):
            if a[i] == 99:
                break
            opcode_set = a[i:i + 4]
            in1 = a[opcode_set[input_1]]
            in2 = a[opcode_set[input_2]]
            if opcode_set[opcode] == 1:
                o = in1 + in2
            else:  # == 2
                o = in1 * in2

            a[opcode_set[output]] = o

        if a[0] == 19690720:
            print(noun, verb)
            print(100 * noun + verb)
