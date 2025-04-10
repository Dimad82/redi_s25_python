def greet(name):
    greeting = f"Hello {name.capitalize()}"
    return greeting

def add(a,b):
    return a + b

# 1, 2, 3, 4, 5
a = [1, 2, 3, 4, 5]
sum = 0
for i in a:
    sum = add(sum, i)
    print(f"sum is now {sum}")

print(sum)


