# Singleton:
# Zastosowanie: Zaimplementuj klasę LibraryCatalog, która zapewnia, że w programie istnieje tylko jedna instancja katalogu. Klasa ta będzie odpowiedzialna za przechowywanie i zarządzanie danymi o książkach.
# Zadanie: Utwórz klasę Singleton i pokaż, jak uzyskać do niej dostęp z różnych części programu.


class LibraryCatalog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()  # private method to initialize the object
        return cls._instance

    def _initialize(self):
        # initialize the object
        self.books = [
            {"title": "Metro2033", "author": "Dmitry Glukhovsky"},
        ]

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def show_books(self):
        for book in self.books:
            print(f"{book['title']} - {book['author']}")

    def delete_book(self, title):
        for book in self.books:
            if book["title"] == title:
                try:
                    self.books.remove(book)
                    print(f"Book {title} deleted")
                except ValueError:
                    print(f"Book {title} not found")


# Example of usage
c1 = LibraryCatalog()
c2 = LibraryCatalog()

c1.add_book("Harry Potter", "J.K. Rowling")
c2.add_book("The Witcher", "Andrzej Sapkowski")

c1.show_books()

# Check if c1 and c2 are the same object
print(c1 is c2)