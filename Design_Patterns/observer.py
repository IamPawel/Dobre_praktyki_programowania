# Observer:
# Zastosowanie: Skonfiguruj system powiadomień, w którym użytkownicy mogą zapisywać się na powiadomienia o wypożyczeniu lub zwrocie książek. LibraryCatalog będzie działał jako podmiot, a użytkownicy jako obserwatorzy.
# Zadanie: Zaimplementuj wzorzec obserwatora, aby powiadamiać użytkowników o określonych zdarzeniach (np. książka, którą chcą, staje się dostępna).


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, title, event):
        print(f"User {self.name} notified: '{title}' has been {event}.")
