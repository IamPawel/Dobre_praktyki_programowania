import pytest
from unittest.mock import create_autospec
from main import (
    PaymentProcessor,
    PaymentGateway,
    TransactionStatus,
    TransactionResult,
)


@pytest.fixture
def mock_gateway():
    """Tworzenie mocka dla PaymentGateway"""
    return create_autospec(PaymentGateway)


@pytest.fixture
def processor(mock_gateway):
    """Tworzenie instancji PaymentProcessor z mockiem PaymentGateway"""
    return PaymentProcessor(mock_gateway)


def test_processPayment_success(processor, mock_gateway):
    """Test udanej transakcji płatności"""
    mock_gateway.charge.return_value = TransactionResult(
        True, "123", "Płatność zakończona sukcesem"
    )

    result = processor.processPayment("user1", 100.0)

    assert result.success
    assert result.transactionId == "123"
    assert result.message == "Płatność zakończona sukcesem"
    mock_gateway.charge.assert_called_once_with("user1", 100.0)


def test_processPayment_failure(processor, mock_gateway):
    """Test nieudanej transakcji płatności"""
    mock_gateway.charge.return_value = TransactionResult(
        False, "123", "Niepowodzenie płatności"
    )

    result = processor.processPayment("user1", 100.0)

    assert not result.success
    assert result.transactionId == "123"
    assert result.message == "Niepowodzenie płatności"
    mock_gateway.charge.assert_called_once_with("user1", 100.0)


def test_processPayment_invalid_amount(processor):
    """Test transakcji z błędną kwotą"""
    with pytest.raises(ValueError):
        processor.processPayment("user1", -50.0)


def test_refundPayment_success(processor, mock_gateway):
    """Test udanego zwrotu płatności"""
    mock_gateway.refund.return_value = TransactionResult(
        True, "123", "Zwrot zakończony sukcesem"
    )

    result = processor.refundPayment("123")

    assert result.success
    assert result.transactionId == "123"
    assert result.message == "Zwrot zakończony sukcesem"
    mock_gateway.refund.assert_called_once_with("123")


def test_getPaymentStatus_completed(processor, mock_gateway):
    """Test statusu transakcji jako COMPLETED"""
    mock_gateway.getStatus.return_value = TransactionStatus.COMPLETED

    status = processor.getPaymentStatus("123")

    assert status == TransactionStatus.COMPLETED
    mock_gateway.getStatus.assert_called_once_with("123")


def test_getPaymentStatus_invalid_transactionId(processor):
    """Test z niepoprawnym identyfikatorem transakcji"""
    with pytest.raises(ValueError):
        processor.getPaymentStatus("")
