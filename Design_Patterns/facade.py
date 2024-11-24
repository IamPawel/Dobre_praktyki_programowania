# Facade:
# Zastosowanie: Stwórz klasę LibraryInterface, która zapewnia uproszczony interfejs do wykonywania typowych operacji, takich jak wyszukiwanie książek, wypożyczanie książki i jej zwracanie. Klasa ta będzie wywoływać złożone podsystemy, takie jak LibraryCatalog i UserManagement.
# Zadanie: Zaimplementuj wzorzec fasady, aby uprościć interakcję z podsystemami biblioteki.
from library_class import LibraryCatalog


class LibraryInterface:
    def __init__(self):
        self.catalog = LibraryCatalog()

    def add_book(self, title, author):
        self.catalog.add_book(title, author)

    def show_books(self):
        books = self.catalog.show_books()
        return books

    def delete_book(self, title):
        self.catalog.delete_book(title)

    def available_books(self):
        books = [book for book in self.catalog.books if book["is_available"]]
        print(books)

    def find_by_author(self, author):
        books = [book for book in self.catalog.books if book["author"] == author]
        return print(books)

    def who_wrote(self, title):
        book = next(
            (book for book in self.catalog.books if book["title"] == title), None
        )
        if book:
            print(f"Book: {title} was written by {book['author']}.")
        else:
            print(f"Book with title '{title}' not found.")


# Usage
library_interface = LibraryInterface()
library_interface.add_book("Book1", "Author1")
library_interface.add_book("Book2", "Author1")
library_interface.add_book("Book3", "Author2")
library_interface.add_book("Book4", "Author2")
library_interface.add_book("Book5", "Author1")
library_interface.add_book("Book6", "Author2")
library_interface.add_book("Book7", "Author1")
library_interface.add_book("Book8", "Author1")
library_interface.add_book("Book9", "Author1")

# show available books
print("All a books:")
library_interface.available_books()

# search by author
print("Books by Author1:")
library_interface.find_by_author("Author1")

# who wrote?
print("Book8 was written by:")
library_interface.who_wrote("Book8")
