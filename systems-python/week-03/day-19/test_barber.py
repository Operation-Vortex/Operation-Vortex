import pytest
from barber import Barber

@pytest.mark.parametrize("amount, expected", [
    (100, 100),
    (200, 200),
    (50, 50),
    (0, 0),
])
def test_receive_payment_various_amounts(barber, amount, expected):
    # Act
    barber.receive_payment(amount)

    # Assert
    assert barber.get_earnings() == expected

@pytest.fixture
def barber():
    # Arrange
    return Barber("Kwame", "0241234567")

def test_receive_payment_increases_earnings(barber):
  

    # Act
    barber.receive_payment(100) 

    # Assert
    assert barber.get_earnings() == 100

def test_multiple_payments_accumulate(barber):
    # Act
    barber.receive_payment(100)
    barber.receive_payment(200)

    # Assert
    assert barber.get_earnings() == 300


def test_correct_payment_updates_earnings(barber):
    # Act
    barber.receive_payment(200)
    barber.correct_payment(180, "entered wrong amount")

    # Assert
    assert barber.get_earnings() == 180


def test_correct_payment_rejects_negative(barber):
    # Act
    barber.receive_payment(200)
    barber.correct_payment(-50, "trying to go negative")

    # Assert
    assert barber.get_earnings() == 200


def test_str_representation(barber):
    barber.receive_payment(100)
    result = str(barber)
    assert "Kwame" in result
    assert "100" in result


def test_repr_representation(barber):
    result = repr(barber)
    assert "Kwame" in result
    assert "0241234567" in result