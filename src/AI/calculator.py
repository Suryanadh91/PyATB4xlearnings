def add(x, y): return x + y


def subtract(x, y): return x - y


def multiply(x, y): return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    else:
        return x / y


print("--- Smart Calculator ---")

while True:
    print("\n Smart Calculator \nselect an action from below\n1. Sum\n2. Subtraction\n3. Multiply\n4. Divide\n5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        except ValueError:
            print("Invalid input: Please enter numbers only.")

    else:
        print("Invalid Choice! Please pick a number between 1 and 5.")