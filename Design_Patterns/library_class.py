class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
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
