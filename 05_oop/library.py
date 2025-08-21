class Book: 
    
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):      
        return f"{self.title}"

class Library:

    def __init__(self):
        self.my_library = []

    def add_book(self, new_book):
        self.my_library.append(new_book)

    def borrow_book(self, book_title):
        for book in self.my_library:
           if book.title == book_title and book.availability == "available":  # We check 2 conditions in the same time
            book.availability = "unavailable"    # Immediately changing of the status after match. 
            print(f"\nYou borrowed book: {book_title}.")
            break
        else:       # Block else will execute only if for loop won't reach break statement. Good Python practice. 
            print(f"{book_title} is not available.")

    def return_book(self, returned_book_title):
        for book in self.my_library:
            if book.title == returned_book_title:
                book.availability = "available"
                print(f"\nThank you for returning book: {returned_book_title}")
                break
        else: 
            print(f"Book {returned_book_title} does not belong to this Library.")

my_library = Library()

book1 = Book("Killer", "Antonio Morales", "available")
book2 = Book("Vibe Coding", "Pierre Alt", "available")
book3 = Book("Python for everyone", "Luis Windows", "available")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print("Books in library:")

for book in my_library.my_library:     # We use for loop to print out only titles of the books. 
    print(book)

my_library.borrow_book("Vibe Coding")

my_library.return_book("Vibe Coding")
