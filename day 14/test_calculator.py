import pytest
from calculator import add, divide, BankAccount

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(10, 0)

# --- Class Tests ---
@pytest.fixture
def account():
    return BankAccount("Alice", 100)

def test_deposit(account):
    assert account.deposit(50) == 150

def test_withdraw(account):
    assert account.withdraw(30) == 70

def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(200)
