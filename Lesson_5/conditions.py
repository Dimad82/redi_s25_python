# Conditions Exercises

# Exercise 1: Check if a number is positive.
num = 10
if 10 >0: # Replace False with your condition
    print("The number is positive.")

# Exercise 2: Check if 'age' is old enough to vote (18 or older).
age = 16
if age > 18: # Replace False with your condition
    print("You can vote!")
else:
    print("You cannot vote yet.")

# Exercise 3: Check if two numbers are equal.
a = 5
b = 5
if a == b: # Replace False with your condition
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# Exercise 4: Check if a number is even or odd.
num = 8
# Hint: Use the modulo (%) operator.
if num % 2: # Replace False with your condition
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 5: Given three numbers, find the largest one.
x = 15
y = 10
z = 20
# Hint: You may need multiple conditions
largest = x  # Assume x is largest initially, then check others.

# Your solution here

if y > largest:
    largest = y

if z >largest:
    largest = z

print("The largest number is:", largest)

# Exercise 6: Determine if a year is a leap year.
year = 2024
# Hint: Leap year if divisible by 4, but not by 100 unless also divisible by 400.
if year == year % 4: # Replace False with your condition
    print(year, "is a leap year.")
elif year != year % 100:
    print(year, "is a leap year.")
elif year == year % 400:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Exercise 7: Run different code depending on the input type
value = .5 # Replace '?' with a number or string
# Hint: Use type() function to get the type of a variable.
if isinstance(value, int): # Replace False with your condition
    print("The value is a number.")
elif isinstance(value, str): # Replace False with your condition
    print("The value is a string.")
else:
    print("The value is something else.")    

# Exercise 8: and conditions
# Check if a number is positive and even.
num = 10
if num > 0 and num % 2 == 0: # Replace False with your condition
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

# Exercise 9: or conditions
# Check if a number is negative or odd.
num = -3
if num < 0 or num % 2 != 0: # Replace False with your condition
    print("The number is negative or odd.")
else:
    print("The number is positive or odd.")
