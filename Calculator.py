def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nSelect operation:")
        print("A. Add")
        print("B. Subtract")
        print("C. Multiply")
        print("D. Divide")
        print("E. Exit")

        choice = input("Enter choice (A/B/C/D/E): ").upper()

        if choice == 'E':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter a letter between A and D.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        if choice == 'A':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 'B':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 'C':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 'D':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

calculator()

calculator()
