class Book:
    def __init__(self, book_title, author, book_id):
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def display_details(self):
        availability = "Available" if self.is_available else "Borrowed"
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

    def display_borrowed_books(self):
        print(f"Member: {self.member_name}, Borrowed Books: {self.borrowed_books}")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_title, author, book_id):
        if book_id not in self.books:
            self.books[book_id] = Book(book_title, author, book_id)
            print(f"Book '{book_title}' added to the library.")
        else:
            print(f"Book ID '{book_id}' already exists.")

    def register_member(self, member_name, member_id):
        if member_id not in self.members:
            self.members[member_id] = Member(member_name, member_id)
            print(f"Member '{member_name}' registered.")
        else:
            print(f"Member ID '{member_id}' already exists.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            if self.books[book_id].borrow():
                self.members[member_id].borrow_book(book_id)
                print(f"Book ID '{book_id}' borrowed by Member ID '{member_id}'.")
            else:
                print(f"Book ID '{book_id}' is not available.")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            self.books[book_id].return_book()
            self.members[member_id].return_book(book_id)
            print(f"Book ID '{book_id}' returned by Member ID '{member_id}'.")
        else:
            print("Invalid member ID or book ID.")

    def display_all_books(self):
        for book in self.books.values():
            book.display_details()

    def display_all_members(self):
        for member in self.members.values():
            member.display_borrowed_books()


# Main Program
def main():
    library = Library()
    while True:
        print("\nIM Library Management System")
        print("1. Add new book")
        print("2. Register as new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Check availability of a book")
        print("6. List all books")
        print("7. List all members")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_title = input("Enter book title: ")
            author = input("Enter author: ")
            book_id = input("Enter book ID: ")
            library.add_book(book_title, author, book_id)
        elif choice == '2':
            member_name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.register_member(member_name, member_id)
        elif choice == '3':
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            library.borrow_book(member_id, book_id)
        elif choice == '4':
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            library.return_book(member_id, book_id)
        elif choice == '5':
            book_id = input("Enter book ID: ")
            if book_id in library.books:
                library.books[book_id].display_details()
            else:
                print("Book ID not found.")
        elif choice == '6':
            library.display_all_books()
        elif choice == '7':
            library.display_all_members()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()