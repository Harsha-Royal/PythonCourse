class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking Now......")

class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
    
    def speak(self): # We *override* the speak method (more on this later)
        super().speak()
        print("Woof!")

class Cat(Animal): # Cat also inherits from Animal
    def speak(self):
        print("Meow!")


A = Dog("scooby")
A.speak()
print(A.location)

#super(): Inside a child class, super() lets you call methods from the parentclass. This is useful when you want to extend the parent’s behavior instead of completely replacing it. It’s especially important when initializing the parent class’s part of a child object

