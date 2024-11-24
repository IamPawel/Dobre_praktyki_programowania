# Singleton:
# Zastosowanie: Zaimplementuj klasę LibraryCatalog, która zapewnia, że w programie istnieje tylko jedna instancja katalogu. Klasa ta będzie odpowiedzialna za przechowywanie i zarządzanie danymi o książkach.
# Zadanie: Utwórz klasę Singleton i pokaż, jak uzyskać do niej dostęp z różnych części programu.
from observer import Observer


class LibraryCatalog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()  # private method to initialize the object
        return cls._instance

    def _initialize(self):
        # initialize the object
        self.books = []
        self.observers = []  # list of observers

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

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["is_available"]:
                    book["is_available"] = False
                    print(f"Book {title} borrowed")
                    self.notify_observers(title, "borrowed")
                else:
                    print(f"Book {title} is not available")
                return
        print(f"Book {title} not found")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:
                if not book["is_available"]:
                    book["is_available"] = True
                    print(f"Book {title} returned")
                    self.notify_observers(title, "returned")
                return
        print(f"Book {title} not found")

    # Observer:
    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, title, event):
        for observer in self.observers:
            observer.update(title, event)
