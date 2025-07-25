import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    
    :param public_key: The public key used for verification.
    :param doc: The XML document to be verified.
    :param signature: The signature to be verified.
    :return: True if the signature is valid, False otherwise.
    """
    try:
        # Parse the XML document
        root = ET.fromstring(doc)
        
        # Serialize the XML document to a string
        serialized_doc = ET.tostring(root, encoding='utf-8', method='xml')
        
        # Load the public key
        pub_key = serialization.load_pem_public_key(public_key)
        
        # Verify the signature
        pub_key.verify(
            signature,
            serialized_doc,
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