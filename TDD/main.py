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


# wyjątki
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
                return TransactionResult(
                    True, result.transactionId, "Płatność zakończona sukcesem"
                )
            else:
                return TransactionResult(
                    False, result.transactionId, "Niepowodzenie płatności"
                )
        except (NetworkException, PaymentException) as e:
            return RefundException(str(e))

    def refundPayment(self, transactionId: str) -> TransactionResult:
        if not transactionId:
            raise ValueError("Nieprawidłowy identyfikator transakcji")

        try:
            result = self.gateway.refund(transactionId)
            if result.success:
                return TransactionResult(
                    True, transactionId, "Zwrot zakończony sukcesem"
                )
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
