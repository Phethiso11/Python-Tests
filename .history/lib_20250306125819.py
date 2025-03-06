class Book:
    def __init__(self, book_title, author, book_id):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.book_title}' has been borrowed.")
        else:
            print(f"Sorry, the book '{self.book_title}' is currently unavailable.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book '{self.book_title}' has been returned.")
        else:
            print(f"The book '{self.book_title}' was not borrowed.")

    def display_details(self):
        availability = "Available" if self.is_available else "Not Available"
        print(f"Title: {self.book_title}, Author: {self.author}, Availability: {availability}")


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
            print(f"You have not borrowed the book with ID: {book_id}.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.member_name}: {', '.join(str(b) for b in self.borrowed_books)}")
        else:
            print(f"{self.member_name} has not borrowed any books.")


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = {} # list of books that t
        self.members = {}

    def add_book(self, book_title, author, book_id):
        new_book = Book(book_title, author, book_id)
        self.books[book_id] = new_book
        print(f"Book '{book_title}' added to the library.")

    def register_member(self, member_name, member_id):
        new_member = Member(member_name, member_id)
        self.members[member_id] = new_member
        print(f"Member '{member_name}' registered.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            if book.is_available:
                book.borrow()
                member.borrow_book(book_id)
            else:
                print(f"Sorry, the book '{book.book_title}' is not available or you are not a member.")
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
                print("This book was not borrowed by you.")
        else:
            print("Invalid member ID or book ID.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display_details()

    def display_all_members(self):
        if not self.members:
            print("No members registered.")
        for member in self.members.values():
            print(f"Member Name: {member.member_name}, Member ID: {member.member_id}")

def main():
 try:
    library = Library("IM Library")

    while True:
        print("\nIM Library Management System")
        print("1. Add New Book")
        print("2. Register as New Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Check Availability of a Book")
        print("6. List All Books")
        print("7. List All Members")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                book_title = input("Enter book title: ")
                author = input("Enter author name: ")
                book_id = input("Enter book ID: ")
                library.add_book(book_title, author, book_id)

            case '2':
                member_name = input("Enter your name: ")
                member_id = input("Enter your member ID: ")
                library.register_member(member_name, member_id)

            case '3':
                member_id = input("Enter your member ID: ")
                book_id = input("Enter book ID to borrow: ")
                library.borrow_book(member_id, book_id)

            case '4':
                member_id = input("Enter your member ID: ")
                book_id = input("Enter book ID to return: ")
                library.return_book(member_id, book_id)

            case '5':
                book_id = input("Enter book ID to check availability: ")
                if book_id in library.books:
                    library.books[book_id].display_details()
                else:
                    print("Book ID not found in the catalog.")

            case '6':
                library.display_all_books()

            case '7':
                library.display_all_members()

            case '8':
                print("Exiting the system.")
                break

            case _:
                print("Invalid choice. Please try again.")
 except:
    print("\nAn error occurred.\nPlease try again")

if __name__ == "__main__":
    main()
