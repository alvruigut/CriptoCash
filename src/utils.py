from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def sign_coin(private_key, data):
    """Firma una moneda utilizando la clave privada del banco."""
    h = SHA256.new(data.encode('utf-8'))
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature

def verify_coin(public_key, coin):
    """Verifica la firma de una moneda y asegura que no ha sido usada previamente."""
    h = SHA256.new(coin['user_id'].encode('utf-8'))
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, coin['signature'])
        return True
    except ValueError:
        return False
