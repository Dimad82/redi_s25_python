class Animal:
    def move(self):
        print("The Animal moves.")

class Bird(Animal):
    def move(self):
        print("The bird flies.")

class Fish(Animal):
    def move(self):
        print("The fish swims.")

bird = Bird()
fish = Fish()

bird.move()
fish.move()