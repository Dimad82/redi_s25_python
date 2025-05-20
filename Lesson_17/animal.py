# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

# Child class for Cat
class Cat(Animal):
    def __init__(self, name, lives_left):
        super().__init__(name)
        self.lives_left = lives_left

# Child class for Dog
class Dog(Animal):
    def __init__(self, name, chew_toys_chewed):
        super().__init__(name)
        self.chew_toys_chewed = chew_toys_chewed

# Creating objects
dog = Dog("Buddy", chew_toys_chewed = 3)
cat = Cat("Whiskers", lives_left = 9)