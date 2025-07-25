from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature

def verificar_firma_reenviable(clave_publica, documento, firma):
    """
    Verifica los elementos XML firmados para tener confianza de que el autor declarado realmente generó este mensaje.
    
    :param clave_publica: Clave pública en formato PEM para verificar la firma.
    :param documento: Documento XML que se desea verificar.
    :param firma: Firma digital del documento.
    :return: True si la firma es válida, False en caso contrario.
    """
    try:
        # Cargar la clave pública
        public_key = load_pem_public_key(clave_publica.encode())
        
        # Verificar la firma
        public_key.verify(
            firma,
            documento.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False