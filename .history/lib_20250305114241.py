class Book:
    def __init__(self, book_title, author, book_id):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.book_title}' borrowed successfully.")
        else:
            print(f"Book '{self.book_title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.book_title}' returned successfully.")
        else:
            print(f"Book '{self.book_title}' was not borrowed.")

    def display_details(self):
        availability = "Available" if self.is_available else "Not Available"
        print(f"Title: {self.book_title}, Author: {self.author}, Status: {availability}")


class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            print("You did not borrow this book.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.member_name} has borrowed the following books:")
            for book_id in self.borrowed_books:
                print(book_id)
        else:
            print(f"{self.member_name} has not borrowed any books.")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_title, author, book_id):
        if book_id not in self.books:
            new_book = Book(book_title, author, book_id)
            self.books[book_id] = new_book
            print(f"Book '{book_title}' added to the library.")
        else:
            print(f"Book ID {book_id} already exists in the catalog.")

    def register_member(self, member_name, member_id):
        if member_id not in self.members:
            new_member = Member(member_name, member_id)
            self.members[member_id] = new_member
            print(f"Member '{member_name}' registered successfully.")
        else:
            print(f"Member ID {member_id} is already registered.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if book.is_available:
                book.borrow()
                member.borrow_book(book_id)
            else:
                print(f"Book '{book.book_title}' is not available.")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if book_id in member.borrowed_books:
                book.return_book()
                member.return_book(book_id)
            else:
                print(f"Member '{member.member_name}' did not borrow this book.")
        else:
            print("Invalid member ID or book ID.")

    def display_all_books(self):
        print("Books in Library:")
        for book in self.books.values():
            book.display_details()

    def display_all_members(self):
        print("Library Members:")
        for member in self.members.values():
            print(f"Name: {member.member_name}, ID: {member.member_id}")


# Main Program

def menu():
    library = Library()

    while True:
        print("\n--- IM Library Management System ---")
        print("1. Add new book")
        print("2. Register new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Check availability of a book")
        print("6. List all books")
        print("7. List all members")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_title = input("Enter book title: ")
            author = input("Enter author name: ")
            book_id = input("Enter book ID: ")
            library.add_book(book_title, author, book_id)
        
        elif choice == '2':
            member_name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.register_member(member_name, member_id)
        
        elif choice == '3':
            member_id = input("Enter your member ID: ")
            book_id = input("Enter the book ID you want to borrow: ")
            library.borrow_book(member_id, book_id)
        
        elif choice == '4':
            member_id = input("Enter your member ID: ")
            book_id = input("Enter the book ID you want to return: ")
            library.return_book(member_id, book_id)
        
        elif choice == '5':
            book_id = input("Enter the book ID to check availability: ")
            if book_id in library.books:
                library.books[book_id].display_details()
            else:
                print("Book ID not found.")
        
        elif choice == '6':
            library.display_all_books()
        
        elif choice == '7':
            library.display_all_members()
        
        elif choice == '8':
            print("Thank you for using IM Library Management System.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
