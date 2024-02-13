# Exceptions = Errors

try:
    print(x)
except:
    print("An error occurred")
finally:
    print("success")

a = 20
b = 0
try:
    print(a / b)
except:
    print("ZeroDivisionError occurred")

    # User defined functions
try:
    def multiply(c, d):
        return c * d


    print(multiply(6, 5))
except:
    print("An error occurred")
finally:
    print("success")
