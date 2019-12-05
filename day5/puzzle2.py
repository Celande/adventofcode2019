"""
Make assembler great again
"""

def get_on_mode(mode, array, value):
    if mode == '0':  # position mode
        return int(array[value])
    # value mode, default is 1
    return value

def get_params_modes(opcode, array, index, modes):
    if opcode in ('1', '2', '7', '8'):  # 3 parameters
        return map(int, a[index + 1: index + 4]), modes.ljust(3, '0')
    if opcode in ('3', '4'):  # 1 parameter
        return int(a[index + 1]), modes.ljust(1, '0')
    if opcode in ('5', '6'):  # 2 parameters
        return map(int, a[index + 1: index + 3]), modes.ljust(2, '0')

# get inputs
# manipulating strings so it is easier to loop on
main_input = '5'
main_output = None
l = ''
with open('input2.txt', 'r') as f:
    l = f.read()

# 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
# output 999 if input < 8
# output 1000 if input == 8
# output 1001 if input > 8
a = [e for e in l.split(',')]

# loop on inputs
i = 0
while i < len(a):
    if a[i] == '99':  # stop if 99
        break
    # get right number of parameters depending on the opcode
    instructions = a[i]
    opcode = instructions[-1]
    modes = instructions[:-2][::-1]  # can read it from left to right

    # apply instructions
    if opcode == '1':  # addition
        params, modes = get_params_modes(opcode, a, i, modes)
        a[params[2]] = str(
            get_on_mode(modes[0], a, params[0]) \
            + get_on_mode(modes[1], a, params[1])
        )
        i += 4
    elif opcode == '2':  # multiplication
        params, modes = get_params_modes(opcode, a, i, modes)
        a[params[2]] = str(
            get_on_mode(modes[0], a, params[0]) \
            * get_on_mode(modes[1], a, params[1])
        )
        i += 4
    elif opcode == '3':  # store main_input at position p
        param, modes = get_params_modes(opcode, a, i, modes)
        a[param] = main_input
        i += 2
    elif opcode == '4':  # make main_output the value at position p
        param, modes = get_params_modes(opcode, a, i, modes)
        main_output = get_on_mode(modes[0], a, param)
        i += 2
    elif opcode == '5':  # jump if true
        params, modes = get_params_modes(opcode, a, i, modes)
        if get_on_mode(modes[0], a, params[0]) != 0:
            i = get_on_mode(modes[1], a, params[1])
        else:
            i += 3
    elif opcode == '6':  # jump if false
        params, modes = get_params_modes(opcode, a, i, modes)
        if get_on_mode(modes[0], a, params[0]) == 0:
            i = get_on_mode(modes[1], a, params[1])
        else:
            i += 3
    elif opcode == '7':  # less than
        params, modes = get_params_modes(opcode, a, i, modes)
        if get_on_mode(modes[0], a, params[0]) < get_on_mode(modes[1], a, params[1]):
            a[params[2]] = '1'
        else:
            a[params[2]] = '0'
        i += 4
    elif opcode == '8':  # equals
        params, modes = get_params_modes(opcode, a, i, modes)
        if get_on_mode(modes[0], a, params[0]) == get_on_mode(modes[1], a, params[1]):
            a[params[2]] = '1'
        else:
            a[params[2]] = '0'
        i += 4

# result
print(main_output)
