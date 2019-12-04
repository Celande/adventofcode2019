def is_increase(nb):
    # checking that the next digit is >= to the previous
    array = map(int, str(nb))
    prev = array[0]
    for now in array[1:]:
        if now < prev:
            return False
        prev = now
    return True

def has_double(nb):
    # checking that there is at least one double digit
    array = map(int, str(nb))
    prev = array[0]
    for now in array[1:]:
        if now == prev:
            return True
        prev = now
    return False

testing = (
    122345, 111123, 111111,  # ok
    135679, 223450, 123789  # not ok
)

puzzle_input = '240920-789857'
min_val, max_val = map(int, puzzle_input.split('-'))

result = 0
for nb in range(min_val, max_val):
    if is_increase(nb) and has_double(nb):
        result += 1

print(result)
