def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
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

    # Extract the signed data and the signature
    signed_data = root.find('.//SignedInfo').text
    signature_value = root.find('.//SignatureValue').text

    # Verify the signature
    try:
        public_key.verify(
            signature_value.encode(),
            signed_data.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False