# 1. Klasa PaymentProcessor:



#    •    Metody:

#    •    processPayment(userId, amount)

#    •    Opis: Przetwarza płatność dla danego użytkownika na określoną kwotę.

#    •    Parametry:

#    •    userId (String): Identyfikator użytkownika.

#    •    amount (double): Kwota do zapłaty.

#    •    Zwraca: TransactionResult (obiekt zawierający informacje o wyniku transakcji).

#    •    refundPayment(transactionId)

#    •    Opis: Dokonuje zwrotu dla podanej transakcji.

#    •    Parametry:

#    •    transactionId (String): Identyfikator transakcji do zwrotu.

#    •    Zwraca: TransactionResult.

#    •    getPaymentStatus(transactionId)

#    •    Opis: Pobiera status płatności dla określonej transakcji.

#    •    Parametry:

#    •    transactionId (String): Identyfikator transakcji.

#    •    Zwraca: TransactionStatus (enum z wartościami PENDING, COMPLETED, FAILED).

#    •    Funkcjonalności:

#    •    Walidacja danych wejściowych:

#    •    Sprawdzenie, czy amount jest dodatnia.

#    •    Sprawdzenie, czy userId i transactionId nie są puste.

#    •    Obsługa wyjątków:

#    •    Obsługa wyjątków rzucanych przez PaymentGateway i odpowiednie reagowanie (np. ponowienie próby, logowanie błędu).

#    •    Logowanie:

#    •    Rejestrowanie informacji o sukcesie lub niepowodzeniu płatności.

#    •    Logowanie szczegółów błędów w przypadku wyjątków.



# 2. Interfejs PaymentGateway:



#    •    Metody:

#    •    charge(userId, amount)

#    •    Opis: Obciąża konto użytkownika określoną kwotą.

#    •    Parametry:

#    •    userId (String): Identyfikator użytkownika.

#    •    amount (double): Kwota do obciążenia.

#    •    Zwraca: TransactionResult.

#    •    Może rzucić wyjątki: NetworkException, PaymentException.

#    •    refund(transactionId)

#    •    Opis: Dokonuje zwrotu dla podanej transakcji.

#    •    Parametry:

#    •    transactionId (String): Identyfikator transakcji.

#    •    Zwraca: TransactionResult.

#    •    Może rzucić wyjątki: NetworkException, RefundException.

#    •    getStatus(transactionId)

#    •    Opis: Pobiera status transakcji.

#    •    Parametry:

#    •    transactionId (String): Identyfikator transakcji.

#    •    Zwraca: TransactionStatus.

#    •    Może rzucić wyjątki: NetworkException.

#    •    Klasy pomocnicze:

#    •    TransactionResult:

#    •    Pola:

#    •    success (boolean): Informuje, czy transakcja się powiodła.

#    •    transactionId (String): Identyfikator transakcji.

#    •    message (String): Opcjonalna wiadomość z dodatkową informacją.

#    •    TransactionStatus (enum):

#    •    Wartości: PENDING, COMPLETED, FAILED.

#    •    Wyjątki:

#    •    NetworkException: Rzucany w przypadku problemów z siecią.

#    •    PaymentException: Rzucany w przypadku błędów płatności.

#    •    RefundException: Rzucany w przypadku błędów podczas zwrotu.



# Wymagania dotyczące testów:



# 1. Implementacja z użyciem TDD:



#    •    Testy dla processPayment:

#    •    Prawidłowe przetworzenie płatności.

#    •    Niepowodzenie płatności z powodu braku środków.

#    •    Obsługa wyjątków NetworkException i PaymentException.

#    •    Walidacja nieprawidłowych danych wejściowych (np. ujemna kwota).

#    •    Testy dla refundPayment:

#    •    Prawidłowe dokonanie zwrotu.

#    •    Niepowodzenie zwrotu z powodu nieistniejącej transakcji.

#    •    Obsługa wyjątków NetworkException i RefundException.

#    •    Testy dla getPaymentStatus:

#    •    Pobranie poprawnego statusu transakcji.

#    •    Obsługa nieistniejącej transakcji.

#    •    Obsługa wyjątków NetworkException.



# 2. Użycie mocków i stubów:



#    •    Mockowanie PaymentGateway:

#    •    Symulowanie różnych odpowiedzi metod charge, refund i getStatus.

#    •    Konfiguracja zwracanych wartości TransactionResult i TransactionStatus.

#    •    Stubbowanie zachowań:

#    •    Definiowanie predefiniowanych odpowiedzi na podstawie wejściowych parametrów.

#    •    Symulowanie rzucania wyjątków przez metody PaymentGateway.



# 3. Użycie spy:



#    •    Weryfikacja wywołań:

#    •    Sprawdzenie, czy metody PaymentGateway zostały wywołane z oczekiwanymi parametrami.

#    •    Weryfikacja liczby wywołań poszczególnych metod.

#    •    Logowanie:

#    •    Użycie spy do weryfikacji, czy odpowiednie komunikaty są logowane.



# 4. Logowanie i obsługa wyjątków:



#    •    Testowanie logowania:

#    •    Upewnienie się, że sukcesy i błędy są poprawnie logowane.

#    •    Weryfikacja, że komunikaty błędów zawierają odpowiednie informacje.

#    •    Obsługa wyjątków:

#    •    Upewnienie się, że wyjątki z PaymentGateway nie powodują przerwania działania PaymentProcessor.

#    •    Sprawdzenie, czy wyjątki są obsługiwane i przekazywane w odpowiedni sposób.





# Wskazówki:



#    •    Podejście TDD:

#    •    Zacznij od napisania testu jednostkowego dla najmniejszej funkcjonalności.

#    •    Zaimplementuj minimalny kod potrzebny do przejścia testu.

#    •    Refaktoryzuj kod i testy, jeśli to konieczne.

#    •    Powtórz proces dla kolejnych funkcjonalności.

#    •    Scenariusze testowe:

#    •    Pokryj testami zarówno przypadki sukcesu, jak i różne rodzaje błędów.

#    •    Upewnij się, że wszystkie możliwe wyjątki są odpowiednio obsłużone.

#    •    Dobre praktyki:

#    •    Utrzymuj czytelność i przejrzystość kodu.

#    •    Komentuj kod tam, gdzie jest to konieczne dla zrozumienia logiki.

#    •    Staraj się pisać testy, które są łatwe w utrzymaniu i rozszerzaniu.
from typing import Optional
from enum import Enum

class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class TransactionResult:
    def __init__(self, success: bool, transactionId: str, message: Optional[str] = ""):
        self.success = success
        self.transactionId = transactionId
        self.message = message
        

#wyjątki
class NetworkException(Exception):
    pass

class PaymentException(Exception):
    pass

class RefundException(Exception):
    pass



class PaymentGateway:
    def charge(self, user_id: str, amount: float) -> TransactionResult:
        return TransactionResult(True, "123", "Płatność zakończona sukcesem")

    def refund(self, transaction_id: str) -> TransactionResult:
        return TransactionResult(True, {transaction_id}, "Operacja zakończona sukcesem")

    def getStatus(self, transaction_id: str) -> TransactionStatus:
        return TransactionStatus.COMPLETED

class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def processPayment(self, userId: str, amount: float) -> TransactionResult:
        if not userId or amount <= 0:
            raise ValueError("Nieprawidłowy użytkownik lub kwota")
        
        try:
            result = self.gateway.charge(userId, amount)
            if result.success:
                return TransactionResult(True, result.transactionId, "Płatność zakończona sukcesem")
            else:
                return TransactionResult(False, result.transactionId, "Niepowodzenie płatności")
        except (NetworkException, PaymentException) as e:
            return RefundException(str(e))
        



    def refundPayment(self, transactionId: str) -> TransactionResult:
        if not transactionId:
            raise ValueError("Nieprawidłowy identyfikator transakcji")
        
        try:
            result = self.gateway.refund(transactionId)
            if result.success:
                return TransactionResult(True, transactionId, "Zwrot zakończony sukcesem")
            else:
                return TransactionResult(False, transactionId, "Niepowodzenie zwrotu")
        except (NetworkException, RefundException) as e:
            raise RefundException(str(e))
        
    def getPaymentStatus(self, transactionId: str) -> TransactionStatus:
        if not transactionId:
            raise ValueError("Nieprawidłowy identyfikator transakcji")
        
        try:
            status = self.gateway.getStatus(transactionId)
            return status
        except NetworkException as e:
            raise NetworkException(str(e))
        
        



