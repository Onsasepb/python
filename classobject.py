# Class is a blueprint of an object
# An object is an instance of a class

class Person:
    # Properties/Attributes/Characteristics
    name = "Bob"
    age = 23
    location = "Westlands"

    def speak(self):
        print("Person is speaking")


accountant = Person()  # Instantiating an object
print(accountant.age)

accountant.speak()
