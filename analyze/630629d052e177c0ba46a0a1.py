def verificar_firma_reenviable(clave_publica, documento, firma):
    """
    Verifica los elementos XML firmados para tener confianza de que el autor declarado realmente generó este mensaje.
    """
    from lxml import etree
    from xmlsec import SignatureContext, Key, constants

    # Cargar el documento XML
    doc = etree.fromstring(documento)

    # Crear un contexto de firma
    ctx = SignatureContext()

    # Cargar la clave pública
    key = Key.from_string(clave_publica, constants.KeyDataFormatPem, constants.KeyTypePublic)
    ctx.key = key

    # Buscar la firma en el documento
    signature_node = doc.find('.//{http://www.w3.org/2000/09/xmldsig#}Signature')

    if signature_node is None:
        raise ValueError("No se encontró la firma en el documento.")

    # Verificar la firma
    try:
        ctx.verify(signature_node)
        return True
    except Exception as e:
        return False