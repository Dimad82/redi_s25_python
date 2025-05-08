class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = dog("Buddy", 2)
dog2 = dog("Muddy", 3)   

print(f"{dog1.name} is {dog1.age} years old") 
print(f"{dog2.name} is {dog2.age} years old") 