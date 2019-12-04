def is_increase(nb):
    # checking that the next digit is >= to the previous one
    array = map(int, str(nb))
    prev = array[0]
    for now in array[1:]:
        if now < prev:
            return False
        prev = now
    return True

def has_double(nb):
    array = map(int, str(nb))
    prev = array[0]
    for now in array[1:]:
        if now == prev:
            return True
        prev = now
    return False

def are_doubles_matching(nb):
    # checking that there is at least one double digits
    # and that there is at least one double digit not
    # in a bigger group
    string = str(nb)
    array = []
    tmp = string[0]
    for now in string[1:]:
        if tmp[0] == now:
            tmp += now
        else:
            array.append(tmp)
            tmp = now
    array.append(tmp)

    for i in array:
        if len(i) == 2:
            return True
    return False

testing = (
    112233, 111122,  # ok
    135679, 223450, 123789, 123444  # not ok
)

puzzle_input = '240920-789857'
min_val, max_val = map(int, puzzle_input.split('-'))

result = 0
for nb in range(min_val, max_val):
    if is_increase(nb) and are_doubles_matching(nb):
        result += 1

print(result)
