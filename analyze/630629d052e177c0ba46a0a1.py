def verificar_firma_reenviable(clave_publica, documento, firma):
    """
    Verifica los elementos XML firmados para tener confianza de que el autor declarado realmente generó este mensaje.
    """
    try:
        # Importar las librerías necesarias
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.exceptions import InvalidSignature
        
        # Verificar la firma usando la clave pública
        clave_publica.verify(
            firma,
            documento.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # Si no se lanza excepción, la firma es válida
        return True
        
    except InvalidSignature:
        # Si se lanza InvalidSignature, la firma no es válida
        return False
    except Exception as e:
        # Cualquier otro error en la verificación
        print(f"Error al verificar firma: {str(e)}")
        return False