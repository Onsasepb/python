# A simple calculator that performs all the operations
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
operator = input("Enter operator:")
if operator == "+":
    print("result is", a + b)

if operator == "-":
    print("result is", a - b)

if operator == "*":
    print("result is", a * b)

if operator == "/":
    print("result is", a / b)
