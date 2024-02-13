# While loop
# Incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing values
x = 105
while x >= 100:
    print(x)
    x -= 1

# Break statement
y = 1
while y <= 5:
    print(y)
    if y == 3:
        break
    y += 1

# Continue
count = 19
while count < 25:
    count += 1
    if count == 23:
        continue
    print(count)

# For loop
languages = ["Python", "C++", "Kotlin"]
for lang in languages:
    print(lang)

# Range of values
for z in range(6):
    print(z)
for y in range(20, 31):
    print(y)

for i in range(30, 41, 2):
    print(i)
h = "innovation"
for p in (
        h):
    print(p)
