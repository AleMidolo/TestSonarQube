import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    """
    # Load the public key
    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )
    
    # Parse the XML document
    root = ET.fromstring(doc)
    
    # Create a canonical representation of the XML
    canonical_xml = ET.tostring(root, encoding='utf-8', method='xml')
    
    # Verify the signature
    try:
        public_key.verify(
            signature,
            canonical_xml,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False