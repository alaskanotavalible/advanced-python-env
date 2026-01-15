a = float(input("First number: "))
operation = input("Operation: ")
b = float(input("Second number: "))

if operation == "/" and b == 0:
    print("Division by zero is not allowed")
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)