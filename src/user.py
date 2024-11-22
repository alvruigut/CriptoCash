
class User:
    def __init__(self, user_id, bank):
        print(f"Creando usuario con ID: {user_id}")  # Traza
        self.user_id = user_id
        self.bank = bank

    def withdraw_coin(self):
        """El usuario solicita una moneda al banco"""
        print(f"Solicitando moneda para el usuario {self.user_id}...")  # Traza
        return self.bank.create_coin(self.user_id)

    def send_coin(self, coin, merchant, receiver_user_id):
        """El usuario transfiere una moneda al comerciante"""
        print(f"Enviando moneda al comerciante: {coin}")  # Traza
        message = merchant.receive_payment(coin, receiver_user_id)  
        print(f"Resultado del pago: {message}")  # Traza
        return message
