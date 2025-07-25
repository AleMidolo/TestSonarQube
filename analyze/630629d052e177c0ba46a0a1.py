def verify_relayable_signature(public_key, doc, signature):
    """
    हस्ताक्षरित XML तत्वों को सत्यापित करें ताकि यह सुनिश्चित किया जा सके 
    कि दावा किया गया लेखक ने वास्तव में यह संदेश उत्पन्न किया है।
    """
    from lxml import etree
    from xmlsec import SignatureContext, verify, KeyData, Signature

    # Load the XML document
    root = etree.fromstring(doc)

    # Create a signature context
    ctx = SignatureContext()

    # Load the public key
    key_data = KeyData()
    key_data.load_public_key(public_key)
    ctx.key = key_data

    # Find the signature in the document
    signature_node = root.find('.//Signature')
    if signature_node is None:
        raise ValueError("Signature not found in the document.")

    # Verify the signature
    signature = Signature(signature_node)
    try:
        ctx.verify(signature)
        return True
    except Exception as e:
        return False