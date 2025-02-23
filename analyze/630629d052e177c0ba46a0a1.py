import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    # Load the public key
    public_key = serialization.load_pem_public_key(public_key)

    # Parse the XML document
    root = ET.fromstring(doc)

    # Extract the signed data (assuming it's in a specific element)
    signed_data = root.find('.//SignedData').text

    # Verify the signature
    try:
        public_key.verify(
            signature,
            signed_data.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False