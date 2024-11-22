from database import Database

class Merchant:
    def __init__(self, name, bank):
        print(f"Creando comerciante {name}...")  # Traza
        self.name = name
        self.bank = bank
        self.db = Database()
        print(f"Comerciante {name} creado con éxito.")  # Traza

    def receive_payment(self, coin, receiver_user_id):
        """El comerciante recibe un pago y lo verifica con el banco"""
        print(f"Recibiendo pago de la moneda: {coin}")  # Traza
        is_valid, message = self.bank.verify_coin(coin)
        print(f"Resultado de la verificación: {message}")  # Traza
        if is_valid:
            return f"Pago recibido correctamente. {message}"
        else:
            return f"Pago fallido: {message}"

    def deposit_coin(self, coin, sender_user_id, receiver_user_id):
        """Deposita una moneda en el banco y registra la transacción"""
        print(f"Depósito de moneda iniciado. Moneda: {coin}, De: {sender_user_id}, A: {receiver_user_id}")  # Traza
        is_valid, message = self.bank.verify_coin(coin)
        if is_valid:
            coin_id = self.db.get_unused_coin()[0]  
            print(f"Registrando transacción de la moneda ID {coin_id}...")  # Traza
            self.db.record_transaction(sender_user_id, receiver_user_id, coin_id)
            self.bank.mark_coin_as_used(coin_id)
            print("Depósito completado y transacción registrada.")  # Traza
            return "Moneda depositada correctamente en el banco."
        else:
            print(f"Depósito fallido: {message}")  # Traza
            return message
