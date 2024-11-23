# Adapter:
# Zastosowanie: Wyobraź sobie, że system biblioteczny musi importować dane o książkach z różnych formatów (np. JSON, CSV). Stwórz klasę adaptera, która pozwoli na przetwarzanie i integrację różnych formatów danych do standardowego formatu używanego w LibraryCatalog.
# Zadanie: Zaimplementuj wzorzec adaptera, który może czytać dane książek z różnych formatów (JSON, XML, CSV) i przekształcać je na standardowy format.

import json
import csv
import xml.etree.ElementTree as ET
from singleton import LibraryCatalog


class Adapter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.catalog = LibraryCatalog()

    def detect_format(self):
        file_path = self.file_path
        if file_path.endswith(".json"):
            return self._load_json()
        if file_path.endswith(".csv"):
            return self._load_csv()
        if file_path.endswith(".xml"):
            return self._load_xml()
        raise ValueError(f"Unknown format: {file_path}")

    def import_books(self):
        books = self.detect_format()
        for book in books:
            self.catalog.add_book(book["title"], book["author"])

    def _load_json(self):
        with open(self.file_path, "r") as file:
            books = json.load(file)
        return books

    def _load_csv(self):
        books = []
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                books.append({"title": row["title"], "author": row["author"]})
        return books

    def _load_xml(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        books = []
        for book in root.findall("book"):
            title = book.find("title").text
            author = book.find("author").text
            books.append({"title": title, "author": author})
        return books


# Import JSON
Adapter("Books/books.json").import_books()

# Import CSV
Adapter("Books/books.csv").import_books()

# Import XML
Adapter("Books/books.xml").import_books()


LibraryCatalog().show_books()
