def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    from lxml import etree
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend

    # Parse the XML document
    try:
        root = etree.fromstring(doc)
    except etree.XMLSyntaxError:
        return False

    # Extract the signed content from the XML
    signed_info = root.find('.//SignedInfo')
    if signed_info is None:
        return False

    # Canonicalize the signed info
    signed_info_c14n = etree.tostring(signed_info, method='c14n')

    # Verify the signature
    try:
        public_key.verify(
            signature,
            signed_info_c14n,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False