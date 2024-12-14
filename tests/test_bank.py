import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bank import Bank
from user import User
from merchant import Merchant

@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def user(bank):
    return User("user123", bank)

@pytest.fixture
def merchant(bank):
    return Merchant("Comercio A", bank)

def test_create_and_verify_coin(bank, user):
    coin = user.withdraw_coin()
    
    is_valid, message = bank.verify_coin(coin)
    
    assert is_valid == True
    assert message == "Moneda verificada correctamente"

def test_double_spending(bank, user):
    coin = user.withdraw_coin()
    

    bank.verify_coin(coin)  
    
    is_valid = bank.verify_coin(coin)  
    
   
    assert  not is_valid == False

def test_payment_flow(bank, user, merchant):
    coin = user.withdraw_coin()
    
    payment_message = user.send_coin(coin, merchant, "Comercio A") 
    
    assert "Pago recibido correctamente" in payment_message
    
    deposit_message = merchant.deposit_coin(coin, user.user_id, merchant.name)
    
    assert "Moneda depositada correctamente en el banco" in deposit_message


def test_invalid_coin(bank, user):
    invalid_coin = {"user_id": "user123", "signature": b"invalid_signature"}
    
    is_valid, message = bank.verify_coin(invalid_coin)
    
    assert is_valid == False
    assert message == "Firma inválida"
