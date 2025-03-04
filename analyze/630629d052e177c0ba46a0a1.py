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
            
        # Convert signature from base64 if needed
        import base64
        if isinstance(signature, str):
            signature = base64.b64decode(signature)
            
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
        # Log error if needed
        print(f"Signature verification failed: {str(e)}")
        return False