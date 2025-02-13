def verify_relayable_signature(public_key, doc, signature):
    from lxml import etree
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

    # Load the public key
    public_key = serialization.load_pem_public_key(public_key)

    # Verify the signature
    try:
        # Extract the signed XML elements
        signed_info = doc.find('.//SignedInfo')
        signed_info_canonical = etree.tostring(signed_info, method='c14n')

        # Verify the signature using the public key
        public_key.verify(
            signature,
            signed_info_canonical,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False