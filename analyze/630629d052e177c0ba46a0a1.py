def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    from lxml import etree

    # Load the public key
    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )

    # Parse the XML document
    root = etree.fromstring(doc)

    # Extract the signature element
    signature_element = root.find(".//{http://www.w3.org/2000/09/xmldsig#}SignatureValue")
    if signature_element is None:
        raise ValueError("Signature element not found in the document.")

    # Get the signed data
    signed_data = etree.tostring(root, method="c14n", exclusive=True, with_comments=False)

    # Verify the signature
    try:
        public_key.verify(
            signature,
            signed_data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False