class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}.")
        elif self.age < other.age:
            print(f"{self.name} is younger than {other.name}")
        else:
            print(f"{self.name} and {other.name} are the same age.")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.compare_age(person2)

