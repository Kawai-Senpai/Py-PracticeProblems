
'''
Design a simple library system using OOP. Create classes ‘Book’, ‘ Author’, and ‘Library’. 
The ‘Book’ class should have attributes for book details (title, ISBN, etc.). 
The ‘Author’ class should have attributes for author details (name, birthdate, etc.). 
The ‘Library’ class should manage a collection of books and authors, allowing users to borrow and return books
'''
# The ‘Book’ class should have attributes for book details (title, ISBN, etc.). 
class Book:
    
    def __init__(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by '{self.author}' (ISBN:{self.isbn})"

#The ‘Author’ class should have attributes for author details (name, birthdate, etc.).
class Author:

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f"'{self.name} (born {self.birthday})'"

#The ‘Library’ class should manage a collection of books and authors, allowing users to borrow and return books
class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return f"Book {book} is sucessfully borrowed"
            
        return "Book not available"
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                return f"Book {book} is sucessfully returned"
            
        return "Book not not found or not borrowed"
    
    def show_books(self):
        available_books = []
        for book in self.books:
            if not book.is_borrowed:
                available_books.append(str(book))
        return available_books
    

#Test
author1 = Author("Bob", "25-05-2001")
book1 = Book("Bob's Book", "1234", author1)

library = Library()
library.add_book(book1)

#Before borrowing
print("Before borrowing >")
print(library.show_books())

#borrowing book
print("Borrowing book >")
print(library.borrow_book("1234"))

#after borrowing
print("After borrowing >")
print(library.show_books())

#returning book
print("Returning book >")
print(library.return_book("1234"))

#After returning
print("After returning >")
print(library.show_books())