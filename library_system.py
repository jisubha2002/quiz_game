class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = True  # By default, a new book is available
    
    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}"
    
    def mark_unavailable(self):
        self.available = False
    
    def mark_available(self):
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_books = 0  # To be overridden by subclasses
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            print(f"Error: {self.name} has reached the maximum borrowing limit of {self.max_books} books.")
            return False
        
        if not book.available:
            print(f"Error: '{book.title}' is already checked out.")
            return False
        
        book.mark_unavailable()
        self.borrowed_books.append(book)
        print(f"'{book.title}' has been successfully borrowed by {self.name}.")
        return True
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"Error: '{book.title}' is not borrowed by {self.name}.")
            return False
        
        book.mark_available()
        self.borrowed_books.remove(book)
        print(f"'{book.title}' has been successfully returned by {self.name}.")
        return True
    
    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")

class Student(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.max_books = 3  # Students can borrow up to 3 books

class Teacher(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.max_books = 5  # Teachers can borrow up to 5 books

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    print(f"Cannot remove '{book.title}' as it is currently checked out.")
                    return False
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return True
        print(f"Book with ID {book_id} not found.")
        return False
    
    def find_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not found_books:
            print(f"No books found with title containing '{title}'.")
        return found_books
    
    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        print(f"Member with ID {member_id} not found.")
        return None
    
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            return False
        
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            print(f"Book with ID {book_id} not found.")
            return False
        
        return member.borrow_book(book)
    
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            return False
        
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            print(f"Book with ID {book_id} not found.")
            return False
        
        return member.return_book(book)
    
class Librarian:
    def __init__(self, library):
        self.library = library
    
    def add_new_book(self, book_id, title, author, year):
        new_book = Book(book_id, title, author, year)
        self.library.add_book(new_book)
    
    def register_new_member(self, member_type, member_id, name):
        if member_type.lower() == "student":
            new_member = Student(member_id, name)
        elif member_type.lower() == "teacher":
            new_member = Teacher(member_id, name)
        else:
            print("Invalid member type. Please specify 'student' or 'teacher'.")
            return None
        
        self.library.register_member(new_member)
        return new_member
    
    def process_borrowing(self, member_id, book_id):
        return self.library.borrow_book(member_id, book_id)
    
    def process_return(self, member_id, book_id):
        return self.library.return_book(member_id, book_id)
    
# Create a library
my_library = Library()

# Create a librarian to manage the library
librarian = Librarian(my_library)

# Add some books
librarian.add_new_book(1, "Python book", "s.k roy", 2019)
librarian.add_new_book(2, "C++", "Danis R", 2008)
librarian.add_new_book(3, " geo polytcise", "E.s sen", 1994)

# Register members
student = librarian.register_new_member("student", 101, "rabindra")
teacher = librarian.register_new_member("teacher", 201, "prof.Alok sir")

# Borrow books
librarian.process_borrowing(101, 1)  
librarian.process_borrowing(201, 3)  

# Try to borrow more than allowed
librarian.process_borrowing(101, 3)  
librarian.process_borrowing(101, 2) 

# Return a book
librarian.process_return(101, 1)  

# List borrowed books
print("\nBorrowed books:")
for member in my_library.members:
    member.list_borrowed_books()

# Search for books
print("\nSearch results for 'Python':")
for book in my_library.find_book_by_title("Python"):
    print(book)