lst = [0, 1, 0, 12, 3]

if min(lst) == 0:
    result = []
    zero = 0
    for x in lst:
        if x != 0:
            result.append(x)
        else:
            zero += 1
    result += [0] * zero
    lst = result

print(lst)
