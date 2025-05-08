# Variables Exercises

# Replace (?) with the right answer

# Exercise 1: Create a variable named 'age' and assign your age to it.
age = "42"
print("Your age is:", age)

# Exercise 2: Create a variable 'name' with your first name.
name = "Ivan"
print("Hello,", name)

# Exercise 3: Create two variables, 'x' and 'y'. Assign numbers to them, then create a third variable 'sum' that adds x and y.
x = "1"
y = "2"
sum = x + y
print("Sum:", sum)

# Exercise 4: Swap the values of two variables (a and b).
a = 5
b = 10
# Hint: Use a third temporary variable

print("Before swapping: a =", a, "b =", b)

# Your solution here
a = 10
b = 5

print("After swapping: a =", a, "b =", b)

# Exercise 5: Given a temperature in Celsius, convert it to Fahrenheit.
celsius = 20
# Formula: fahrenheit = (celsius * 9/5) + 32

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Exercise 6: Calculate the area of a rectangle from given width and height.
width = 10
height = 5
area = width * height
print("Area of rectangle:", area)

# Exercise 7: Identify the type of different variables using type()
number = 42
text = "Hello"
decimal = 3.14
is_valid = True

# Your solution here (print the type of each variable)
print(type(number))
print(type(text))
print(type(decimal))
print(type(is_valid))

# Exercise 8: Change the type of a variable by reassigning it
value = 100
print("Original value:", value, "Type:", type(value))
# Now change value to a string
value = "100"
print("After conversion:", value, "Type:", type(value))

# Exercise 9: Type conversion - convert a string to an integer
age_string = "25"
# Convert age_string to an integer and add 5 to it
age_int = 25
age_after_5_years = age_int + 5
print(f"Age in 5 years: {age_after_5_years}")

# Exercise 10: Demonstrate dynamic typing by changing variable types
dynamic_var = 50
print("dynamic_var is initially:", dynamic_var, "Type:", type(dynamic_var))

# Change it to a float
dynamic_var = 50.5
print("dynamic_var is now:", dynamic_var, "Type:", type(dynamic_var))

# Change it to a string
dynamic_var = "50"
print("dynamic_var is finally:", dynamic_var, "Type:", type(dynamic_var))

# Exercise 11: Working with different types
num = 10
text = "The number is: "
# What should you do if you want something like "The number is: 10"?
result = 10
print("The number is:",result)
