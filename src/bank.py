from database import Database
from Crypto.PublicKey import ECC
from utils import sign_coin, verify_coin

class Bank:
    def __init__(self):
        self.db = Database()  
        self.private_key = ECC.generate(curve='P-256')
        self.public_key = self.private_key.public_key()

    def get_public_key(self):
        """Devuelve la clave pública del banco"""
        return self.public_key.export_key(format='PEM')

    def create_coin(self, user_id):
        """Genera una moneda firmada digitalmente y la almacena en la base de datos"""
        signature = sign_coin(self.private_key, user_id)
        self.db.add_coin(user_id, signature)
        return {'user_id': user_id, 'signature': signature}

    def verify_coin(self, coin):
        """Verifica si la moneda es válida y no ha sido gastada"""
        if verify_coin(self.public_key, coin):
            stored_coin = self.db.get_unused_coin()
            if stored_coin:
                return True, "Moneda verificada correctamente"
            else:
                return False, "Doble gasto detectado"  
        return False, "Firma inválida"  


    def mark_coin_as_used(self, coin_id):
        """Marca una moneda como utilizada después de un depósito exitoso"""
        self.db.mark_coin_as_used(coin_id)
