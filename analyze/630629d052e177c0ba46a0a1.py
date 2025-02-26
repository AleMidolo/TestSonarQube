def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, Signature

    # Parse the XML document
    root = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key = KeyData()
    key.load(public_key, xmlsec.KeyFormat.PEM)

    # Add the key to the context
    ctx.key = key

    # Find the signature in the document
    signature_node = root.find('.//Signature')
    if signature_node is None:
        raise ValueError("Signature not found in the document.")

    # Verify the signature
    try:
        verify(signature_node, ctx)
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False