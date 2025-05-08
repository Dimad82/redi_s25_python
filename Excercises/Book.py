class Book:
    def __init__(self, title, author="Unknown", year="Unknown"):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("Python Essentials")
book2 = Book("Learn Java", "John Doe", 2022)

print(f"{book1.title} by {book1.author}, published in {book1.year}")                     
print(f"{book2.title} by {book2.author}, published in {book2.year}")