# First class
class Dog:

    def sound(self):
        print("Dog says: Woof Woof")


# Second class
class Cat:

    def sound(self):
        print("Cat says: Meow Meow")


# Creating objects
dog1 = Dog()
cat1 = Cat()

# Same method call with different objects
dog1.sound()
cat1.sound()