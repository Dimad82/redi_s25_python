# Loops Exercises
# Exercise 1: Print numbers from 1 to 5.
# Your solution here
numbers = [1,2,3,4,5]
for x in numbers: # Replace False with your loop
  print(x)

# Exercise 2: Calculate the sum of numbers from 1 to 10.
# Simple calculation using a loop (GTPT)
total = 0
for i in range(1, 11):  # Iterating through numbers 1 to 10
    total += i
print("The sum is:", total)

# Alternatively, using Python's built-in sum() function (GTPT)
total = sum(range(1, 11))
print("The sum is:", total) 


# Exercise 3: Print all even numbers from 2 to 20.
for num in range(2, 21, 2):
    print(num)

# Exercise 4: Print the multiplication table for 7 (up to 10).
# Your solution here
for i in range(1, 11):  # Loop from 1 to 10
    print(f"7 x {i} = {7 * i}")

# Exercise 5: Find the factorial of a number.
num = 5
factorial = 1
# Hint: Factorial of 5 is 5 × 4 × 3 × 2 × 1
# Your solution here
print(f"Factorial of {num} is {factorial}")

# Exercise 6: Iterate through a string and count vowels.
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
# Your solution here
print(f"Number of vowels: {count}")

# Exercise 7: Use a while loop to print numbers from 1 to 5.
num = 1
while num <= 5:
    print(num)
    num += 1
  

# Exercise 8: Use a while loop to continually divide a number by 2 until it's less than 1.
num = 100
steps = 0
while num >= 1:
    num /= 2
    steps += 1

print(f"Final number: {num}, Steps taken: {steps}")

# Exercise 9: Break out of a loop when a certain condition is met.
# Hint: to get a number between 1 and 20 use:
# num = random.randint(1, 20)
# Find the first even number and count how many iterations it took
import random
count = 0
# Your solution here

# Exercise 10: Use continue to skip certain values in a loop.
# Print all numbers from 1 to 10 except multiples of 3
# Your solution here
