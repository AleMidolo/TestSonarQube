def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    try:
        # Import required crypto libraries
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        from cryptography.exceptions import InvalidSignature
        
        # Convert doc to bytes if it's not already
        if isinstance(doc, str):
            doc = doc.encode('utf-8')
            
        # Load the public key if it's in PEM format
        if isinstance(public_key, str):
            public_key = load_pem_public_key(public_key.encode())
            
        # Verify the signature
        try:
            public_key.verify(
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
            
    except Exception as e:
        # Return False for any other errors during verification
        return False