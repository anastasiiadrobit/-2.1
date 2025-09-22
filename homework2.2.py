x = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
y = float(input("Second number: "))

if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    if x == 0:
        print("Error:Cannot divide by zero!")
    else:
        print("Result:", x / y)
