def get_on_mode(mode, array, value):
    if mode == '0':  # position mode
        return int(array[value])
    # value mode, default is 1
    return value

def get_params_modes(opcode, array, index, modes):
    if opcode in ('1', '2'):
        return map(int, a[index + 1: index + 4]), modes.ljust(3, '0')
    if opcode in ('3', '4'):
        return int(a[index + 1]), '0'

# get inputs
# manipulating strings so it is easier to loop on
main_input = '1'
main_output = None
l = ''
with open('input1.txt', 'r') as f:
    l = f.read()

# '1002,4,3,4,33' -> '1002,4,3,4,99'
# '1101,100,-1,4,0' -> '1101,100,-1,4,99'
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
        main_output = a[param]
        i += 2

# result
print(main_output)
