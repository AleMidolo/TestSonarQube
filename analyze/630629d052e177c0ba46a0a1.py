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

    # Verificar la firma
    try:
        ctx.verify(firma)
        return True
    except Exception as e:
        print(f"Error al verificar la firma: {e}")
        return False