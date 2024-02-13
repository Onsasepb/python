temperature = 32
if temperature > 37:
    print("It is hot")
else:
    print("It is cold")

# A programme that prints the largest number among three numbers
num1 = 35
num2 = 79
num3 = 22
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

    # A programme that checks whether a number is even or odd
number = 55

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
num = 2

# A programme that checks whether a number is a prime

p = 0

if p > 1:
    # check for factors
    for i in range(2, p):
        if (p % i) == 0:
            print(p, "is not a prime number.")

            break
    else:
        print(p, "is a prime number.")

# If the input number is less than or equal to 1, then it is not prime
else:
    print(p, "is not a prime number.")
