def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    from lxml import etree
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

    # Load the public key
    public_key = serialization.load_pem_public_key(public_key)

    # Parse the XML document
    root = etree.fromstring(doc)

    # Extract the signed content and the signature
    signed_content = etree.tostring(root, method='xml', exclusive=True)
    signature_bytes = bytes.fromhex(signature)

    # Verify the signature
    try:
        public_key.verify(
            signature_bytes,
            signed_content,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False