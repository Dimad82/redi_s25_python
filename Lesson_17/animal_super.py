# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak_with_subtitles(self, type):
        return "The {type} says: "

# Child class - Dog inherits from Animal
class Dog(Animal):
    def speak_with_subtitles(self):
        return super().speak_with_subtitles("Woof! Woof!")
    
# Child class - Cat inherits from Animal
class Cat(Animal):
    def speak_with_subtitles(self):
        return "Miau"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())