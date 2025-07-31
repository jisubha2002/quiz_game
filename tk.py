'''import tkinter as tk
from tkinter import messagebox, ttk
from library_system import Library, Librarian  # Import your existing classes

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.library = Library()
        self.librarian = Librarian(self.library)
        
        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        # Book Management Tab  
        self.book_frame = ttk.Frame(self.notebook, width=600, height=400)
        self.member_frame = ttk.Frame(self.notebook, width=600, height=400)
        self.transaction_frame = ttk.Frame(self.notebook, width=600, height=400)
        
        self.notebook.add(self.book_frame, text="Book Management")
        self.notebook.add(self.member_frame, text="Member Management")
        self.notebook.add(self.transaction_frame, text="Transactions")
        
        self.setup_book_tab()
        self.setup_member_tab()
        self.setup_transaction_tab()
    
    def setup_book_tab(self):
        # Add Book Section
        ttk.Label(self.book_frame, text="Add New Book").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        labels = ["ID:", "Title:", "Author:", "Year:"]
        self.book_entries = {}
        
        for i, label in enumerate(labels):
            ttk.Label(self.book_frame, text=label).grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = ttk.Entry(self.book_frame)
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.book_entries[label[:-1].lower()] = entry
        
        ttk.Button(self.book_frame, text="Add Book", command=self.add_book).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Book List Section
        self.book_tree = ttk.Treeview(self.book_frame, columns=("ID", "Title", "Author", "Year", "Status"), show="headings")
        self.book_tree.heading("ID", text="ID")
        self.book_tree.heading("Title", text="Title")
        self.book_tree.heading("Author", text="Author")
        self.book_tree.heading("Year", text="Year")
        self.book_tree.heading("Status", text="Status")
        self.book_tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        ttk.Button(self.book_frame, text="Refresh List", command=self.refresh_book_list).grid(row=7, column=0, columnspan=2)
    
    def add_book(self):
        try:
            book_id = int(self.book_entries['id'].get())
            title = self.book_entries['title'].get()
            author = self.book_entries['author'].get()
            year = int(self.book_entries['year'].get())
            
            self.librarian.add_new_book(book_id, title, author, year)
            messagebox.showinfo("Success", "Book added successfully!")
            self.refresh_book_list()
            
            # Clear entries
            for entry in self.book_entries.values():
                entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data for all fields!")
    
    def refresh_book_list(self):
        # Clear existing items
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)
        
        # Add books from library
        for book in self.library.books:
            status = "Available" if book.available else "Checked Out"
            self.book_tree.insert("", "end", values=(book.book_id, book.title, book.author, book.year, status))


    def __init__(self, root):
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        # Book Management Tab  
        self.member_frame = ttk.Frame(self.notebook, width=600, height=400)
        #self.member_frame = ttk.Frame(self.notebook, width=600, height=400)
        #self.transaction_frame = ttk.Frame(self.notebook, width=600, height=400)

        self.setup_member_tab()

    def setup_member_tab(self):
        # Add Member Section
        ttk.Label(self.member_frame, text="Add New Member").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        labels = ["member ID:", "name:", "max books:"]
        self.member_entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self.member_frame, text=label).grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(self.member_frame)
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.member_entries[label[:-1].lower()] = entry
        ttk.Button(self.member_frame, text="Add member", command=self.add_member).grid(row=5, column=0, columnspan=2, pady=10)

        self.member_tree = ttk.Treeview(self.member_frame, columns=("member ID", "name", "max books"), show="headings")
        self.member_tree.heading("member ID", text="member ID")
        self.member_tree.heading("name", text="name")
        self.member_tree.heading("max books", text="max books")

    def add_member(self):
        try:
            member_id = int(self.member_entries['member id'].get())
            name = self.member_entries['name'].get()
            max_books = int(self.member_entries['max books'].get())
        
            self.librarian.add_new_member(member_id, name, max_books)
            messagebox.showinfo("Success", "Member added successfully!")
        
        # Clear entries
            for entry in self.member_entries.values():
             entry.delete(0, tk.END)
        except ValueError:
          messagebox.showerror("Error", "Please enter valid data for all fields!")

    def setup_transaction_tab(self):
        # Similar structure for borrowing/returning books
        pass
def setup_member_tab(self):
    # Add Member Section
    ttk.Label(self.member_frame, text="Register New Member").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    # Member Type Radio Buttons
    self.member_type = tk.StringVar(value="student")
    ttk.Label(self.member_frame, text="Member Type:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Radiobutton(self.member_frame, text="Student", variable=self.member_type, value="student").grid(row=1, column=1, padx=5, pady=5, sticky="w")
    ttk.Radiobutton(self.member_frame, text="Teacher", variable=self.member_type, value="teacher").grid(row=1, column=1, padx=5, pady=5, sticky="e")
    
    # Member ID and Name
    labels = ["ID:", "Name:"]
    self.member_entries = {}
    
    for i, label in enumerate(labels):
        ttk.Label(self.member_frame, text=label).grid(row=i+2, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(self.member_frame)
        entry.grid(row=i+2, column=1, padx=10, pady=5)
        self.member_entries[label[:-1].lower()] = entry
    
    ttk.Button(self.member_frame, text="Register Member", command=self.register_member).grid(row=4, column=0, columnspan=2, pady=10)
    
    # Member List Section
    self.member_tree = ttk.Treeview(self.member_frame, columns=("ID", "Name", "Type", "Borrowed Books"), show="headings")
    self.member_tree.heading("ID", text="ID")
    self.member_tree.heading("Name", text="Name")
    self.member_tree.heading("Type", text="Type")
    self.member_tree.heading("Borrowed Books", text="Borrowed Books")
    self.member_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    ttk.Button(self.member_frame, text="Refresh List", command=self.refresh_member_list).grid(row=6, column=0, columnspan=2)

def register_member(self):
    try:
        member_id = int(self.member_entries['id'].get())
        name = self.member_entries['name'].get()
        member_type = self.member_type.get()
        
        if not name:
            raise ValueError("Name cannot be empty")
            
        self.librarian.register_new_member(member_type, member_id, name)
        messagebox.showinfo("Success", "Member registered successfully!")
        self.refresh_member_list()
        
        # Clear entries
        for entry in self.member_entries.values():
            entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", f"Please enter valid data: {str(e)}")

def refresh_member_list(self):
    # Clear existing items
    for item in self.member_tree.get_children():
        self.member_tree.delete(item)
    
    # Add members from library
    for member in self.library.members:
        member_type = "Student" if isinstance(member) else "Teacher"
        borrowed_count = len(member.borrowed_books)
        self.member_tree.insert("", "end", values=(member.member_id, member.name, member_type, borrowed_count))

def setup_transaction_tab(self):
    # Borrow Book Section
    ttk.Label(self.transaction_frame, text="Borrow Book").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    labels = ["Member ID:", "Book ID:"]
    self.borrow_entries = {}
    
    for i, label in enumerate(labels):
        ttk.Label(self.transaction_frame, text=label).grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(self.transaction_frame)
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        self.borrow_entries[label[:-1].lower().replace(" ", "_")] = entry
    
    ttk.Button(self.transaction_frame, text="Borrow Book", command=self.borrow_book).grid(row=3, column=0, columnspan=2, pady=10)
    
    # Return Book Section
    ttk.Label(self.transaction_frame, text="Return Book").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    
    labels = ["Member ID:", "Book ID:"]
    self.return_entries = {}
    
    for i, label in enumerate(labels):
        ttk.Label(self.transaction_frame, text=label).grid(row=i+5, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(self.transaction_frame)
        entry.grid(row=i+5, column=1, padx=10, pady=5)
        self.return_entries[label[:-1].lower().replace(" ", "_")] = entry
    
    ttk.Button(self.transaction_frame, text="Return Book", command=self.return_book).grid(row=7, column=0, columnspan=2, pady=10)
    
    # Transaction History Section
    ttk.Label(self.transaction_frame, text="Transaction History").grid(row=8, column=0, padx=10, pady=10, sticky="w")
    self.transaction_text = tk.Text(self.transaction_frame, height=10, width=60)
    self.transaction_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
    self.transaction_text.config(state=tk.DISABLED)

def borrow_book(self):
    try:
        member_id = int(self.borrow_entries['member_id'].get())
        book_id = int(self.borrow_entries['book_id'].get())
        
        if self.librarian.process_borrowing(member_id, book_id):
            messagebox.showinfo("Success", "Book borrowed successfully!")
            self.refresh_book_list()
            self.refresh_member_list()
            self.log_transaction(f"Member {member_id} borrowed book {book_id}")
        else:
            messagebox.showerror("Error", "Failed to borrow book")
            
        # Clear entries
        for entry in self.borrow_entries.values():
            entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid IDs")

def return_book(self):
    try:
        member_id = int(self.return_entries['member_id'].get())
        book_id = int(self.return_entries['book_id'].get())
        
        if self.librarian.process_return(member_id, book_id):
            messagebox.showinfo("Success", "Book returned successfully!")
            self.refresh_book_list()
            self.refresh_member_list()
            self.log_transaction(f"Member {member_id} returned book {book_id}")
        else:
            messagebox.showerror("Error", "Failed to return book")
            
        # Clear entries
        for entry in self.return_entries.values():
            entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid IDs")

def log_transaction(self, message):
    self.transaction_text.config(state=tk.NORMAL)
    self.transaction_text.insert(tk.END, message + "\n")
    self.transaction_text.config(state=tk.DISABLED)
    self.transaction_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()'''
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        
        # Initialize data storage
        self.books_file = "library_books.json"
        self.books = self.load_books()
        
        # Create GUI elements
        self.create_widgets()
        
    def load_books(self):
        """Load books from JSON file or return empty list if file doesn't exist"""
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_books(self):
        """Save books to JSON file"""
        with open(self.books_file, 'w') as f:
            json.dump(self.books, f, indent=4)
    
    def create_widgets(self):
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs
        self.add_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)
        self.checkout_tab = ttk.Frame(self.notebook)
        self.return_tab = ttk.Frame(self.notebook)
        self.view_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.add_tab, text="Add Book")
        self.notebook.add(self.search_tab, text="Search Books")
        self.notebook.add(self.checkout_tab, text="Check Out Book")
        self.notebook.add(self.return_tab, text="Return Book")
        self.notebook.add(self.view_tab, text="View All Books")
        
        # Add Book Tab
        self.create_add_book_tab()
        
        # Search Books Tab
        self.create_search_books_tab()
        
        # Check Out Book Tab
        self.create_checkout_book_tab()
        
        # Return Book Tab
        self.create_return_book_tab()
        
        # View All Books Tab
        self.create_view_books_tab()
    
    def create_add_book_tab(self):
        """Create widgets for the Add Book tab"""
        # Labels
        ttk.Label(self.add_tab, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="ISBN:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        ttk.Label(self.add_tab, text="Copies:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        
        # Entry fields
        self.title_entry = ttk.Entry(self.add_tab, width=40)
        self.author_entry = ttk.Entry(self.add_tab, width=40)
        self.isbn_entry = ttk.Entry(self.add_tab, width=40)
        self.copies_entry = ttk.Entry(self.add_tab, width=40)
        
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)
        self.isbn_entry.grid(row=2, column=1, padx=5, pady=5)
        self.copies_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Add button
        ttk.Button(self.add_tab, text="Add Book", command=self.add_book).grid(row=4, column=1, pady=10)
        
        # Status label
        self.add_status = ttk.Label(self.add_tab, text="", foreground="green")
        self.add_status.grid(row=5, column=0, columnspan=2)
    
    def create_search_books_tab(self):
        """Create widgets for the Search Books tab"""
        # Search frame
        search_frame = ttk.LabelFrame(self.search_tab, text="Search Criteria")
        search_frame.pack(fill='x', padx=5, pady=5)
        
        # Search options
        ttk.Label(search_frame, text="Search by:").grid(row=0, column=0, padx=5, pady=5)
        self.search_by = tk.StringVar(value="title")
        ttk.Radiobutton(search_frame, text="Title", variable=self.search_by, value="title").grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(search_frame, text="Author", variable=self.search_by, value="author").grid(row=0, column=2, padx=5, pady=5)
        ttk.Radiobutton(search_frame, text="ISBN", variable=self.search_by, value="isbn").grid(row=0, column=3, padx=5, pady=5)
        
        # Search entry
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
        # Search button
        ttk.Button(search_frame, text="Search", command=self.search_books).grid(row=2, column=0, columnspan=4, pady=5)
        
        # Results treeview
        self.search_results = ttk.Treeview(self.search_tab, columns=('title', 'author', 'isbn', 'copies', 'available'), show='headings')
        self.search_results.heading('title', text='Title')
        self.search_results.heading('author', text='Author')
        self.search_results.heading('isbn', text='ISBN')
        self.search_results.heading('copies', text='Total Copies')
        self.search_results.heading('available', text='Available Copies')
        
        self.search_results.column('title', width=200)
        self.search_results.column('author', width=150)
        self.search_results.column('isbn', width=100)
        self.search_results.column('copies', width=80)
        self.search_results.column('available', width=80)
        
        self.search_results.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Status label
        self.search_status = ttk.Label(self.search_tab, text="", foreground="green")
        self.search_status.pack()
    
    def create_checkout_book_tab(self):
        """Create widgets for the Check Out Book tab"""
        # ISBN entry
        ttk.Label(self.checkout_tab, text="ISBN of Book to Check Out:").pack(pady=(10, 0))
        self.checkout_isbn = ttk.Entry(self.checkout_tab, width=40)
        self.checkout_isbn.pack()
        
        # Borrower info
        ttk.Label(self.checkout_tab, text="Borrower Name:").pack(pady=(10, 0))
        self.borrower_name = ttk.Entry(self.checkout_tab, width=40)
        self.borrower_name.pack()
        
        # Checkout button
        ttk.Button(self.checkout_tab, text="Check Out Book", command=self.checkout_book).pack(pady=10)
        
        # Status label
        self.checkout_status = ttk.Label(self.checkout_tab, text="", foreground="green")
        self.checkout_status.pack()
    
    def create_return_book_tab(self):
        """Create widgets for the Return Book tab"""
        # ISBN entry
        ttk.Label(self.return_tab, text="ISBN of Book to Return:").pack(pady=(10, 0))
        self.return_isbn = ttk.Entry(self.return_tab, width=40)
        self.return_isbn.pack()
        
        # Return button
        ttk.Button(self.return_tab, text="Return Book", command=self.return_book).pack(pady=10)
        
        # Status label
        self.return_status = ttk.Label(self.return_tab, text="", foreground="green")
        self.return_status.pack()
    
    def create_view_books_tab(self):
        """Create widgets for the View All Books tab"""
        # Treeview to display all books
        self.all_books_tree = ttk.Treeview(self.view_tab, columns=('title', 'author', 'isbn', 'copies', 'available'), show='headings')
        self.all_books_tree.heading('title', text='Title')
        self.all_books_tree.heading('author', text='Author')
        self.all_books_tree.heading('isbn', text='ISBN')
        self.all_books_tree.heading('copies', text='Total Copies')
        self.all_books_tree.heading('available', text='Available Copies')
        
        self.all_books_tree.column('title', width=200)
        self.all_books_tree.column('author', width=150)
        self.all_books_tree.column('isbn', width=100)
        self.all_books_tree.column('copies', width=80)
        self.all_books_tree.column('available', width=80)
        
        self.all_books_tree.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Refresh button
        ttk.Button(self.view_tab, text="Refresh List", command=self.refresh_books_list).pack(pady=5)
        
        # Populate the treeview
        self.refresh_books_list()
    
    def add_book(self):
        """Add a new book to the library"""
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        copies = self.copies_entry.get().strip()
        
        if not all([title, author, isbn, copies]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            copies = int(copies)
            if copies <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Copies must be a positive integer!")
            return
        
        # Check if ISBN already exists
        for book in self.books:
            if book['isbn'] == isbn:
                messagebox.showerror("Error", "A book with this ISBN already exists!")
                return
        
        # Add the new book
        new_book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'copies': copies,
            'available': copies,
            'checked_out': []
        }
        
        self.books.append(new_book)
        self.save_books()
        
        # Clear fields and show success message
        self.title_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.isbn_entry.delete(0, 'end')
        self.copies_entry.delete(0, 'end')
        
        self.add_status.config(text=f"Book '{title}' added successfully!")
        self.root.after(3000, lambda: self.add_status.config(text=""))
    
    def search_books(self):
        """Search for books based on criteria"""
        search_term = self.search_entry.get().strip().lower()
        search_by = self.search_by.get()
        
        if not search_term:
            messagebox.showwarning("Warning", "Please enter a search term")
            return
        
        # Clear previous results
        for item in self.search_results.get_children():
            self.search_results.delete(item)
        
        # Search and display results
        found_books = []
        for book in self.books:
            if search_term in book[search_by].lower():
                found_books.append(book)
        
        if not found_books:
            self.search_status.config(text="No books found matching your criteria", foreground="red")
            return
        
        for book in found_books:
            self.search_results.insert('', 'end', values=(
                book['title'],
                book['author'],
                book['isbn'],
                book['copies'],
                book['available']
            ))
        
        self.search_status.config(text=f"Found {len(found_books)} book(s)", foreground="green")
    
    def checkout_book(self):
        """Check out a book"""
        isbn = self.checkout_isbn.get().strip()
        borrower = self.borrower_name.get().strip()
        
        if not isbn or not borrower:
            messagebox.showerror("Error", "Both ISBN and borrower name are required!")
            return
        
        # Find the book
        book_found = False
        for book in self.books:
            if book['isbn'] == isbn:
                book_found = True
                if book['available'] <= 0:
                    messagebox.showerror("Error", "No copies of this book are available!")
                    return
                
                # Check if borrower already has this book checked out
                for checkout in book['checked_out']:
                    if checkout['borrower'] == borrower:
                        messagebox.showerror("Error", "This borrower already has a copy of this book!")
                        return
                
                # Check out the book
                book['available'] -= 1
                book['checked_out'].append({
                    'borrower': borrower,
                    'isbn': isbn
                })
                
                self.save_books()
                messagebox.showinfo("Success", f"Book checked out successfully to {borrower}")
                self.checkout_status.config(text=f"Book checked out to {borrower}", foreground="green")
                self.root.after(3000, lambda: self.checkout_status.config(text=""))
                self.checkout_isbn.delete(0, 'end')
                self.borrower_name.delete(0, 'end')
                self.refresh_books_list()
                break
        
        if not book_found:
            messagebox.showerror("Error", "Book with this ISBN not found!")
    
    def return_book(self):
        """Return a checked out book"""
        isbn = self.return_isbn.get().strip()
        
        if not isbn:
            messagebox.showerror("Error", "ISBN is required!")
            return
        
        # Find the book
        book_found = False
        for book in self.books:
            if book['isbn'] == isbn:
                book_found = True
                if len(book['checked_out']) == 0:
                    messagebox.showerror("Error", "This book hasn't been checked out!")
                    return
                
                # Return the book (we'll just return the first one for simplicity)
                book['available'] += 1
                borrower = book['checked_out'][0]['borrower']
                book['checked_out'].pop(0)
                
                self.save_books()
                messagebox.showinfo("Success", f"Book returned successfully by {borrower}")
                self.return_status.config(text=f"Book returned by {borrower}", foreground="green")
                self.root.after(3000, lambda: self.return_status.config(text=""))
                self.return_isbn.delete(0, 'end')
                self.refresh_books_list()
                break
        
        if not book_found:
            messagebox.showerror("Error", "Book with this ISBN not found!")
    
    def refresh_books_list(self):
        """Refresh the list of all books in the View All Books tab"""
        # Clear the treeview
        for item in self.all_books_tree.get_children():
            self.all_books_tree.delete(item)
        
        # Add all books to the treeview
        for book in self.books:
            self.all_books_tree.insert('', 'end', values=(
                book['title'],
                book['author'],
                book['isbn'],
                book['copies'],
                book['available']
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()