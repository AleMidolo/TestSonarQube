def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, KeyInfo

    # Load the XML document
    xml_doc = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key = KeyData()
    key.load(public_key, KeyInfo.X509)

    # Attach the key to the context
    ctx.key = key

    # Find the signature in the document
    signature_node = xml_doc.find('.//{http://www.w3.org/2000/09/xmldsig#}Signature')

    if signature_node is None:
        raise ValueError("Signature not found in the document.")

    # Verify the signature
    try:
        verify(signature_node, ctx)
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False