# Singleton:
# Zastosowanie: Zaimplementuj klasę LibraryCatalog, która zapewnia, że w programie istnieje tylko jedna instancja katalogu. Klasa ta będzie odpowiedzialna za przechowywanie i zarządzanie danymi o książkach.
# Zadanie: Utwórz klasę Singleton i pokaż, jak uzyskać do niej dostęp z różnych części programu.


class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()  # private method to initialize the object
        return cls._instance

    def _initialize(self):
        # initialize the object
        self.books = []

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

    # all books
    def all_books(self):
        books = [book for book in self.books]
        return print(books)

    def available_books(self):
        books = [book for book in self.books if book["is_available"]]
        return print(books)

    # search by title
    def find_by_title(self, title):
        books = [book for book in self.books if book["title"] == title]
        return print(books)

    # search by author
    def find_by_author(self, author):
        books = [book for book in self.books if book["author"] == author]
        return print(books)


# Usage
library = LibraryCatalog()
library.add_book("Book1", "Author1", is_available=True)
library.add_book("Book2", "Author1", is_available=True)
library.add_book("Book3", "Author2", is_available=False)
library.add_book("Book4", "Author2", is_available=True)
library.add_book("Book5", "Author1", is_available=False)
library.add_book("Book6", "Author2", is_available=True)
library.add_book("Book7", "Author1", is_available=False)
library.add_book("Book8", "Author1", is_available=True)
library.add_book("Book9", "Author1", is_available=True)


# initialize iterator
iter = LibraryIterator(library)

print("All books:")
iter.all_books()

print("Available books:")
iter.available_books()

print("Books by Author1:")
iter.find_by_author("Author1")
