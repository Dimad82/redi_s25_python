def compute(n1, n2):
    answer = n1 / n2
    return answer

user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
numbers = []

try:
    numbers.append(int(user_input_1))
    numbers.append(int(user_input_2))

    answer = compute(numbers[0], numbers[1])
    print(f"{num1} / {num2} = {answer}")
except ValueError:
    print(f"Could not convert {user_input_1} or {user_input_2} to proper numbers.")
except ZeroDivisionError:
    print(f"Cannot divide by {user_input_2}. Try entering a non-zero number.")
except Exception as e:
    print(f"The following error occurred: {e}.")    
else:
    print(f"{num1} / {num2} = {answer}")
finally:
    print(f"Thanks for using my application.")