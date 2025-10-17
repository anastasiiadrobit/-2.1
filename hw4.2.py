numbers = [0, 1, 7, 2, 4, 8]

if numbers:
    even_index_sum = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            even_index_sum += numbers[i]

    result = even_index_sum * numbers[-1]
else:

    result = 0

print(result)
