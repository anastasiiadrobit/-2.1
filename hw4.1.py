lst = [0, 1, 0, 12, 3]

if 0 in lst:
    lst = [x for x in lst if x != 0] + [0] * lst.count(0)

print(lst)
