def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, Signature

    # Load the XML document
    xml_doc = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key_data = KeyData()
    key_data.load(public_key, xmlsec.KeyDataFormatPem)
    ctx.key = key_data

    # Find the signature in the document
    signature_node = xml_doc.find('.//Signature')
    if signature_node is None:
        raise ValueError("No signature found in the document.")

    # Verify the signature
    try:
        verify(ctx, signature_node)
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False