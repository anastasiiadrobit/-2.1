import random

num_elements = random.randint(3, 10)
original_list = [random.randint(0, 10) for _ in range(num_elements)]
print("Start list:", original_list)


new_list = [original_list[0], original_list[2], original_list[-2]]
print("New list:", new_list)
