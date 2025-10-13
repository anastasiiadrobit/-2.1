lst = [1, 2, 3, 4, 5]

result = [lst[:(len(lst) + 1) // 2], lst[(len(lst) + 1) // 2:]] if lst else [[], []]

print(result)
