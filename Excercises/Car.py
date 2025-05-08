class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def paint(self, new_color):
        self.color = new_color

car1 = Car("Toyota", "Red", 2022)

car1.paint("Blue")
print(f"The car in now {car1.color}.")