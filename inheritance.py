class Animal:
    def speak(self):
        print("Animal is speaking")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Dog):
    def purr(self):
        print("Cat is purring")


a = Animal()
d = Dog()
c = Cat()
c.speak()
