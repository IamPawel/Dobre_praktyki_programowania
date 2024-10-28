import unittest
from unittest.mock import Mock, create_autospec
from main import (
    PaymentProcessor,
    PaymentGateway,
    TransactionStatus,
    NetworkException,
    PaymentException,
    RefundException,
    TransactionResult,
)


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.mock_gateway = create_autospec(PaymentGateway)
        self.processor = PaymentProcessor(self.mock_gateway)

    def test_processPayment_success(self):
        # udana transakcja
        self.mock_gateway.charge.return_value = TransactionResult(
            True, "123", "Płatność zakończona sukcesem"
        )

        result = self.processor.processPayment("user1", 100.0)

        self.assertTrue(result.success)
        self.assertEqual(result.transactionId, "123")
        self.assertEqual(result.message, "Płatność zakończona sukcesem")
        self.mock_gateway.charge.assert_called_once_with("user1", 100.0)

    def test_processPayment_failure(self):
        # nieudana transakcja
        self.mock_gateway.charge.return_value = TransactionResult(
            False, "123", "Niepowodzenie płatności"
        )

        result = self.processor.processPayment("user1", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "123")
        self.assertEqual(result.message, "Niepowodzenie płatności")
        self.mock_gateway.charge.assert_called_once_with("user1", 100.0)

    def test_processPayment_invalid_amount(self):
        # zła kwota
        with self.assertRaises(ValueError):
            self.processor.processPayment("user1", -50.0)

    def test_refundPayment_success(self):
        # udana operacja zwrotu
        self.mock_gateway.refund.return_value = TransactionResult(
            True, "123", "Zwrot zakończony sukcesem"
        )

        result = self.processor.refundPayment("123")

        self.assertTrue(result.success)
        self.assertEqual(result.transactionId, "123")
        self.assertEqual(result.message, "Zwrot zakończony sukcesem")
        self.mock_gateway.refund.assert_called_once_with("123")

    def test_getPaymentStatus_completed(self):
        # Ustawienie statusu jako COMPLETED
        self.mock_gateway.getStatus.return_value = TransactionStatus.COMPLETED

        status = self.processor.getPaymentStatus("123")

        self.assertEqual(status, TransactionStatus.COMPLETED)
        self.mock_gateway.getStatus.assert_called_once_with("123")

    def test_getPaymentStatus_invalid_transactionId(self):
        # zły identyfikator transakcji
        with self.assertRaises(ValueError):
            self.processor.getPaymentStatus("")


if __name__ == "__main__":
    unittest.main()
