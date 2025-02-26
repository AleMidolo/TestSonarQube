def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, Key

    # Load the XML document
    xml_doc = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key = Key.from_string(public_key, KeyData.PEM)
    ctx.key = key

    # Find the signature node in the XML document
    signature_node = xml_doc.find('.//{http://www.w3.org/2000/09/xmldsig#}Signature')

    if signature_node is None:
        raise ValueError("Signature node not found in the document.")

    # Verify the signature
    try:
        verify(signature_node, ctx)
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False