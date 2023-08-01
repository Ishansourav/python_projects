import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not defined.")
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Multi-Functional Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Sin")
print("8. Cos")
print("9. Tan")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
    print("Invalid choice.")
else:
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print("Error:", str(e))
    elif choice == '5':
        print("Result:", exponentiate(num1, num2))
    elif choice == '6':
        try:
            print("Result:", square_root(num1))
        except ValueError as e:
            print("Error:", str(e))
    elif choice == '7':
        print("Result:", sin(num1))
    elif choice == '8':
        print("Result:", cos(num1))
    elif choice == '9':
        print("Result:", tan(num1))

