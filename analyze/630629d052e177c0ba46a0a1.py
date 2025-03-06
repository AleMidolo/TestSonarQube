from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    """
    try:
        # Load the public key
        pub_key = serialization.load_pem_public_key(public_key)
        
        # Verify the signature
        pub_key.verify(
            signature,
            doc,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False