checked = open('checked.txt', 'r+')
n = checked.readlines()[-1][0:-1]

def is_junior(k, length):
    k_2 = str(k)
    bad_digits = ['0', '3', '5', '6', '7', '9']
    if len(k_2) < length:
        return False
    for char in k_2:
        if char in bad_digits:
            return False
    return True

def cycle_check(cycle, length):
    for number in cycle:
        if is_junior(number, length):
            return False
    return True

cycle = [int(n)]

sufix_length = len(n)

next_sufix = cycle[-1] * 2

flag = 0

while not next_sufix in cycle:
    if flag == 0:
        if len(str(next_sufix)) > sufix_length:
            checked.write(str(next_sufix) + '\n')
            flag = 1
    cycle.append(next_sufix % (10 ** sufix_length))
    next_sufix = (cycle[-1] * 2)


if cycle_check(cycle, sufix_length):
    print(cycle)
    checked.write(str(cycle) + '\n')

checked.close()




