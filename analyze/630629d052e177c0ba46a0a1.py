def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.

    Args:
        public_key (str): The public key used for verification.
        doc (str): The XML document to be verified.
        signature (str): The signature to verify against the document.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    from lxml import etree

    # Load the public key
    pub_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )

    # Parse the XML document
    root = etree.fromstring(doc.encode())

    # Extract the signature element
    signature_element = etree.fromstring(signature.encode())

    # Verify the signature
    try:
        pub_key.verify(
            signature_element.text.encode(),
            etree.tostring(root),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False