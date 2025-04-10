import pyfiglet

def format_text():
    print("Welcome to the text Formatter!")
    text = input("Enter the text you want to format: ")
    formatted_text = pyfiglet.figlet_format(text)
    print("\nHere's your formatted text:\n")
    print(formatted_text)

if __name__ == "__main__":
    format_text()