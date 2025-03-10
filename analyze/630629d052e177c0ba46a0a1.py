from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils

def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
    
    :param public_key: La chiave pubblica in formato PEM.
    :param doc: Il documento XML come stringa.
    :param signature: La firma del documento.
    :return: True se la firma è valida, False altrimenti.
    """
    try:
        # Deserializza la chiave pubblica
        pub_key = serialization.load_pem_public_key(public_key.encode())
        
        # Verifica la firma
        pub_key.verify(
            signature,
            doc.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False