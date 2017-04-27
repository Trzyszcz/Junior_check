n = input()

def is_junior(k):
    bad_digits = ['0', '3', '5', '6', '7', '9']
    for char in k:
        if char in bad_digits:
            return False
    return True

cycle = [int(n)]

sufix_length = len(n)

next_sufix = cycle[-1] * 2

flag = 0

while not next_sufix in cycle:
    if flag == 0:
        if len(str(next_sufix)) > sufix_length:
            print(next_sufix)
            flag = 1
    cycle.append(next_sufix % (10 ** sufix_length))
    next_sufix = (cycle[-1] * 2)

print(cycle)






