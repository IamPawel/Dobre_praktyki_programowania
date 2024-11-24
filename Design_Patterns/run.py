from library_catalog import LibraryCatalog
from factory import UserFactory
import time


librarian = UserFactory.create_user("Kacper", "librarian")

catalog = LibraryCatalog()
catalog.add_book("Harry Potter", "J.K. Rowling", True)

# create book operation for librarian, this generates a notification
catalog.borrow_book("Harry Potter")
time.sleep(3)
catalog.return_book("Harry Potter")
