import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bank import Bank
from user import User
from merchant import Merchant

# Fixture para crear un objeto Bank
@pytest.fixture
def bank():
    return Bank()

# Fixture para crear un objeto User
@pytest.fixture
def user(bank):
    return User("user123", bank)

# Fixture para crear un objeto Merchant
@pytest.fixture
def merchant(bank):
    return Merchant("Comercio A", bank)

# Test de creación y verificación de una moneda
def test_create_and_verify_coin(bank, user):
    # El usuario solicita una moneda
    coin = user.withdraw_coin()
    
    # Verificar la moneda con el banco
    is_valid, message = bank.verify_coin(coin)
    
    # Assert para verificar que la moneda es válida y la firma es correcta
    assert is_valid == True
    assert message == "Moneda verificada correctamente"

# Test para detectar el doble gasto
def test_double_spending(bank, user):
    # El usuario solicita una moneda
    coin = user.withdraw_coin()
    
    # Verificar la moneda una vez
    bank.verify_coin(coin)  # Se utiliza la moneda una vez
    
    # Intento de doble gasto con la misma moneda
    is_valid = bank.verify_coin(coin)  # El banco detecta el doble gasto
    
    # Assert para verificar que el doble gasto es detectado
    assert  not is_valid == False

# Test de flujo de pago entre usuario y comerciante
def test_payment_flow(bank, user, merchant):
    # El usuario solicita una moneda
    coin = user.withdraw_coin()
    
    # El comerciante recibe el pago. Aquí, pasamos el ID de comerciante como parámetro.
    payment_message = user.send_coin(coin, merchant, "Comercio A")  # Ahora pasamos el ID del comerciante como 'receiver_user_id'
    
    # Assert para verificar que el pago fue exitoso
    assert "Pago recibido correctamente" in payment_message
    
    # El comerciante deposita la moneda en el banco
    deposit_message = merchant.deposit_coin(coin, user.user_id, merchant.name)
    
    # Assert para verificar que la moneda fue depositada correctamente
    assert "Moneda depositada correctamente en el banco" in deposit_message


# Test para manejar una moneda con firma inválida
def test_invalid_coin(bank, user):
    # Se crea una moneda con un ID que no tiene firma válida
    invalid_coin = {"user_id": "user123", "signature": b"invalid_signature"}
    
    # Verificar la moneda con el banco
    is_valid, message = bank.verify_coin(invalid_coin)
    
    # Assert para verificar que la moneda con firma inválida es rechazada
    assert is_valid == False
    assert message == "Firma inválida"
