def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    """
    from lxml import etree
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization

    # Load the public key
    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )

    # Parse the XML document
    root = etree.fromstring(doc)

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