lst = [1, 2, 3, 4, 5]

if len(lst) == 0:
    result = [[], []]
else:
    result = [lst[:(len(lst) + 1) // 2], lst[(len(lst) + 1) // 2:]]

print(result)
