import string

user_input = input("Enter two letters separated by a dash (a-c): ")
start, end = user_input.split('-')
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
if start_index <= end_index:
    result = ''.join(letters[start_index:end_index + 1])
else:
    result = ''.join(letters[start_index:] + letters[:end_index + 1])
print(result)
