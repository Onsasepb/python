# Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
is_Python_Interesting = True  # bool

# A variable with multiple values
languages = ["python", "php", "java", "kotlin"]  # list
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Ghana", "China"}  # set
# Dictionary
details = {
    "firstname": "Ashley",
    "course": "MIT",
    "age": 18,
    "nationality": "USA"
}
print(number)
print(num)
print(greeting)
print(is_Python_Interesting)
print(countries)
print(details)
print(details["firstname"])
print(details["nationality"])

# Determining the data type of  variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one datatype to another px
print(float(number))
print(int(num))












# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
