from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizar un enlace (href) de una imagen en partes compuestas.

    :param image_href: href de una imagen
    :returns: una tupla con el formato (image_id, netloc, use_ssl)
    :raises ValueError: Si el enlace no es válido o no puede ser analizado correctamente.
    """
    if not image_href:
        raise ValueError("El enlace de la imagen no puede estar vacío.")
    
    parsed_url = urlparse(image_href)
    
    if not parsed_url.netloc:
        raise ValueError("El enlace de la imagen no contiene un dominio válido.")
    
    image_id = parsed_url.path.strip('/')
    if not image_id:
        raise ValueError("El enlace de la imagen no contiene un identificador válido.")
    
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'
    
    return (image_id, netloc, use_ssl)