def calculate(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"
while True:
    operator = input("Enter your operator(+, -, *, /): ")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    result = calculate(n1, n2, operator)
    print("Result: ", result)

    choice = input("Continue? (y/n): ").lower()
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Close")
        break