# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Child class for Cat
class Cat(Animal):
    def __init__(self, name, age, lives_left):
        super().__init__(name, age)
        self.lives_left = lives_left

    def __str__(self):
        return f"Cat: {self.name}, {self.age} years old, {self.lives_left} lives left"

# Child class for Dog
class Dog(Animal):
    def __init__(self, name, age, chew_toys_chewed):
        super().__init__(name, age)
        self.chew_toys_chewed = chew_toys_chewed

    def __str__(self):
        return f"Dog: {self.name}, {self.age} years old, chewed {self.chew_toys_chewed} toys"

# Creating a list of animals
animals = [
    Cat("Whiskers", 3, 7),
    Dog("Buddy", 5, 20),
    Cat("Mittens", 2, 9),
    Dog("Charlie", 4, 15),
]

# Printing the list of animals
for animal in animals:
    print(animal)


