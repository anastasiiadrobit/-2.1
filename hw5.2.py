while True:
    num1 = float(input("Enter the first number: "))
    op = input("Enter an operation (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("ERROR: Division by zero!".upper())
            continue
    else:
        print("UNKNOWN OPERATION!".title())
        continue

    print(f"Result: {result}".swapcase())

    choice = input("Do you want to continue? (y): ").strip().lower()
    if choice not in ('y',):
        print("Calculator session ended.".center(50, "-"))
        break
