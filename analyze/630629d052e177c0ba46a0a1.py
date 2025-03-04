def verificar_firma_reenviable(clave_publica, documento, firma):
    """
    Verifica los elementos XML firmados para tener confianza de que el autor declarado realmente generó este mensaje.
    """
    try:
        # Importar las librerías necesarias
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.exceptions import InvalidSignature
        
        # Crear el objeto hash SHA256
        hasher = hashes.Hash(hashes.SHA256())
        
        # Actualizar el hash con el contenido del documento
        hasher.update(documento.encode('utf-8'))
        
        # Obtener el valor del hash
        digest = hasher.finalize()
        
        try:
            # Verificar la firma usando la clave pública
            clave_publica.verify(
                firma,
                digest,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
            
        except InvalidSignature:
            return False
            
    except Exception as e:
        print(f"Error al verificar la firma: {str(e)}")
        return False