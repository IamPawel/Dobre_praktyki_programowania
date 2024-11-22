# Factory:
# Zastosowanie: Zaimplementuj UserFactory, która tworzy różne typy obiektów użytkowników (np. Student, Nauczyciel, Bibliotekarz) na podstawie danych wejściowych. Każdy typ użytkownika może mieć różne uprawnienia do wypożyczania książek.
# Zadanie: Utwórz metodę fabryki do generowania różnych typów użytkowników i pokaż, jak fabryka umożliwia elastyczne tworzenie obiektów.


class UserFactory:
    @staticmethod
    def create_user(name, role):
        if role == "student":
            return Student(name)
        if role == "teacher":
            return Teacher(name)
        if role == "librarian":
            return Librarian(name)
        raise ValueError(f"Unknown role: {role}")


class User:
    def __init__(self, name):
        self.name = name


class Student(User):
    def __init__(self, name):  # constructor based class
        super().__init__(name)
        self.role = "student"
        self.permissions = ["show_books", "borrow_book", "return_book"]


class Teacher(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "teacher"
        self.permissions = ["show_books", "borrow_book", "return_book", "add_book"]


class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "librarian"
        self.permissions = ["show_books", "add_book", "remove_book"]


# create users
users = [
    UserFactory.create_user("Paweł", "student"),
    UserFactory.create_user("Kszyszek", "teacher"),
    UserFactory.create_user("Tomek", "librarian"),
]

# show users
for user in users:
    print(
        f"Name: {user.name}, Role: {user.role}, Permissions: {', '.join(user.permissions)}"
    )
