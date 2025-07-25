def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    try:
        # Import required crypto libraries
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        from cryptography.exceptions import InvalidSignature

        # Load the public key if it's in PEM format
        if isinstance(public_key, str):
            public_key = load_pem_public_key(public_key.encode())

        # Convert doc to bytes if it isn't already
        if isinstance(doc, str):
            doc = doc.encode()

        # Convert signature to bytes if it isn't already  
        if isinstance(signature, str):
            signature = bytes.fromhex(signature)

        # Verify the signature
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
        # Log other errors but return False for verification
        print(f"Error verifying signature: {str(e)}")
        return False