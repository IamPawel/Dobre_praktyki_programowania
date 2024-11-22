#Adapter:
#Zastosowanie: Wyobraź sobie, że system biblioteczny musi importować dane o książkach z różnych formatów (np. JSON, CSV). Stwórz klasę adaptera, która pozwoli na przetwarzanie i integrację różnych formatów danych do standardowego formatu używanego w LibraryCatalog.
#Zadanie: Zaimplementuj wzorzec adaptera, który może czytać dane książek z różnych formatów (JSON, XML, CSV) i przekształcać je na standardowy format.

import json
import csv
import xml.etree.ElementTree as ET

#json adapter
class JsonAdapter:
    def __init__(self, json_data):
        self.data = json_data

    def read_books(self):
        books = json.loads(self.data)
        return ["title": book["title"], "author": book["author"] for book in books]