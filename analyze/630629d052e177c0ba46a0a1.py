def verify_relayable_signature(public_key, doc, signature):
    """
    Verifica gli elementi XML firmati per avere la certezza che l'autore dichiarato abbia effettivamente generato questo messaggio.
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, Key

    # Parse the XML document
    root = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key = Key.from_string(public_key, KeyData.KeyFormat.PEM)
    ctx.key = key

    # Find the signature node in the XML
    signature_node = root.find('.//{http://www.w3.org/2000/09/xmldsig#}Signature')

    if signature_node is None:
        raise ValueError("Signature element not found in the document.")

    # Verify the signature
    try:
        verify(signature_node, ctx)
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False