import xml.etree.ElementTree as ET
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    # Load the public key
    public_key = serialization.load_pem_public_key(public_key)

    # Create a hash of the document
    doc_hash = hashlib.sha256(ET.tostring(doc)).digest()

    # Verify the signature
    try:
        public_key.verify(
            signature,
            doc_hash,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False