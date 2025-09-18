num = int(input("Enter 5-digit number: "))

d1 = num % 10
d2 = (num // 10) % 10
d3 = (num // 100) % 10
d4 = (num // 1000) % 10
d5 = (num // 10000) % 10

print(d1, d2, d3, d4, d5, sep="")

