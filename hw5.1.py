import string
import keyword

name = input("Enter a string: ")

if (name in keyword.kwlist or
    name[0].isdigit() or
    any(ch.isupper() for ch in name) or
    any(ch in string.punctuation.replace("_", "") for ch in name) or
    " " in name or
    name.count("_") > 1 or
    not name):
    print(False)
else:
    print(True)
