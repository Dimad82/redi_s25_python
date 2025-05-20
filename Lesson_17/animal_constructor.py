# Parent class
class Animal:
    def __init__(self, name):
        print(f"We're calling the constructor with the name {name}")
        self.name = name
        print(f"Object constructed")

    def speak(self):
        return ""

# Child class - Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"
    
# Child class - Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Miau"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())