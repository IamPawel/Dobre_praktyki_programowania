# Iterator:
# Zastosowanie: Zaimplementuj iterator do przeglądania listy książek w katalogu lub listy użytkowników. Może to być użyte do wyświetlania szczegółów książek lub informacji o użytkownikach w ustrukturyzowany sposób.
# Zadanie: Stwórz wzorzec iteratora, który umożliwia iterację po kolekcji LibraryCatalog zawierającej książki lub UserManagement zarejestrowanych użytkowników.


class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
            return cls._instance

    def _initialize(self):
        # initialize the object
        self.books = [
            {"title": "Book2", "author": "Author2", "is_available": True},
            {"title": "Book1", "author": "Author1", "is_available": False},
            {"title": "Book3", "author": "Author2", "is_available": True},
            {"title": "Book4", "author": "Author1", "is_available": False},
            {"title": "Book5", "author": "Author1", "is_available": True},
            {"title": "Book6", "author": "Author3", "is_available": True},
            {"title": "Book7", "author": "Author3", "is_available": True},
            {"title": "Book8", "author": "Author3", "is_available": False},
            {"title": "Book9", "author": "Author1", "is_available": True},
            {"title": "Book10", "author": "Author2", "is_available": True},
        ]

    def add_book(self, title, author, is_available=True):
        self.books.append(
            {"title": title, "author": author, "is_available": is_available}
        )

    def show_books(self):
        for book in self.books:
            status = "available" if book["is_available"] else "not available"
            print(f"{book['title']} - {book['author']} ({status})")

    def delete_book(self, title):
        for book in self.books:
            if book["title"] == title:
                try:
                    self.books.remove(book)
                    print(f"Book {title} deleted")
                except ValueError:
                    print(f"Book {title} not found")

    def __iter__(self):
        return LibraryIterator(self.books)


class LibraryIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

    def filter_by_author(self, author):
        filtered_books = [book for book in self.books if book["author"] == author]
        return filtered_books

    def filter_available_books(self):
        available_books = [book for book in self.books if book["is_available"]]
        return available_books


# Usage
library_catalog = LibraryCatalog()
print("Books by Author1:")
for book in library_catalog.__iter__().filter_by_author("Author1"):
    print(f"Title: {book['title']}, Author: {book['author']}")

print("Available books:")
for book in library_catalog.__iter__().filter_available_books():
    print(f"Title: {book['title']}, Author: {book['author']}")
