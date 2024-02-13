class Person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = Person("Joe", 34, "male")
accountant = Person("Mary", 32, "female")
doctor = Person("John", 24, "male")

print(teacher.firstname, teacher.age, teacher.gender)
doctor.details()
