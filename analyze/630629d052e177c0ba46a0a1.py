import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
    
    :param public_key: Chiave pubblica in formato PEM.
    :param doc: Documento XML come stringa.
    :param signature: Firma digitale come bytes.
    :return: True se la firma è valida, False altrimenti.
    """
    try:
        # Carica la chiave pubblica
        pub_key = serialization.load_pem_public_key(public_key.encode())
        
        # Estrai il contenuto da firmare dal documento XML
        root = ET.fromstring(doc)
        content_to_sign = ET.tostring(root, encoding='utf-8', method='xml')
        
        # Verifica la firma
        pub_key.verify(
            signature,
            content_to_sign,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Errore durante la verifica della firma: {e}")
        return False