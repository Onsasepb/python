# Inbuilt functions
y = max(67, 45, 57, 45, 23)
print(y)

x = min(67, 867, 87, 86, 9)
print(x)

z = pow(5, 5)
print(z)


# User-defined functions
def details():
    print("Precious")


details()  # Calling a function


# Parameters and arguments
def students(name, course, age):
    print(name, course, age)


students("Precious", "MIT", "17")
students("Sang", "Full stack", "23")


# full name id salary position age
def employees(fullname, idno, salary, position, age):
    print(fullname, idno, salary, position, age)


employees("Onsase Precious", "20949305", "155000", "Administration",   "28")
employees("Purity Joan",     "11492616", "120000", "Manager",          "43")
employees("Joy Kimeli",      "67593658", "110000", "Public Relations", "34")
employees("Mitchelle Limo",  "21857493", "100000", "Microfinance",     "30")
employees("Stacy Limo",      "21547758", "85000",  "Secretary",        "26")
