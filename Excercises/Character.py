class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

# Creating objects
char = Character("Hero")

# Taking damage
char.take_damage(20)
char.take_damage(30)