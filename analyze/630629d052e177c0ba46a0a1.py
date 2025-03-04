def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    """
    try:
        # Import required cryptography libraries
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        from cryptography.exceptions import InvalidSignature
        
        # Convert doc to bytes if not already
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
        # Log error if needed
        print(f"Signature verification failed: {str(e)}")
        return False