from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    
    :param public_key: The public key used for verification.
    :param doc: The document (XML) that was signed.
    :param signature: The signature to verify.
    :return: True if the signature is valid, False otherwise.
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