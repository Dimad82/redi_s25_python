"""
This program is a simple calculator. It uses all the common math operations
to compute answers.

There are 13 issues in this program. Some are logic errors and some are
runtime errors that will throw exceptions. Your task, should you choose to
accept it, is to find them all!

Hint: A separate file lists 13 line numbers. These are where the errors are.
But see if you can spot them first without looking at the hints.
"""


def menu():
    """
    Displays the calculator menu to the terminal and gets the user's
    choice.
    :return: A string containing the menu option the user chose.
    """

    print()
    print("Choose from the following operations:")
    print("    1. Addition")
    print("    2. Subtraction")
    print("    3. Multiplication")
    print("    4. Division")
    print("    5. Modulo")
    print("    6. Integer Division")
    print("    7. Exponent")
    print("    8. Average for four numbers")
    print("    0. Exit")
    option = int(input("Option: "))
    print()
    return option


def get_input():
    """
    Gets input from the user and passes ot back as a tuple to the caller.
    :return: Floating point numbers
    """

    str_input_1 = input("Enter your first number: ")
    str_input_2 = input("Enter your second number: ")
    num_1 = float(str_input_1)
    num_2 = float(str_input_2)
    return num_1, num_2


def main():
    """
    This script drives the program. This contains all the logic to perform
    the calculations once the user chooses which operation they want to perform
    and provides the values for the operation.
    """

    keep_going = True

    while keep_going:
        # Display the menu.
        option = menu()

        # Figure out which option the user chose and do it.
        if option == 1:
            operand1, operand2 = get_input()
            answer = operand1 + operand2
            print(f"Addition: {operand1} + {operand2} = {answer}")
        elif option == 2:
            operand1, operand2 = get_input()
            answer = operand1 - operand2
            print(f"Subtraction: {operand1} - {operand2} = {answer}")
        elif option == 3:
            operand1, operand2 = get_input()
            answer = operand1 + operand2
            print(f"Multiplication: {operand1} * {operand2} = {answer}")
        elif option == 4:
            operand1, operand2 = get_input()
            answer = operand1 / operand1
            print(f"Division: {operand1} / {operand2} = {answer}")
        elif option == 4:
            operand1, operand2 = get_input()
            answer = operand1 % operand2
            print(f"Modulo: {operand1} % {operand2} = {answer}")
        elif option == 6:
            operand1, operand2 = get_input()
            int_operand1 = int(operand1)
            int_operand2 = int(operand2)
            answer = int_operand1 / int_operand2
            print(
                f"Integer Division: {int_operand1} // {int_operand2} = {answer}")
        elif option == 7:
            operand1, operand2 = get_input()
            answer = operand1 * operand2
            print(f"Exponent: {operand1} ** {operand2} = {answer}")
        elif option == 8:
            operand1, operand2 = get_input()
            operand3 = float(input("Enter your third number: "))
            operand4 = float(input("Enter your fourth number: "))
            answer = operand1 + operand2 + operand3
            average = answer / 4
            print(
                f"Average: The sum of your numbers is {answer} and the average is {average}.")
        else:
            print(f"\nYou entered an invalid option of {option}.")


if __name__ == "__main__":
    main()