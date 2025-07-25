from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizar un enlace (href) de una imagen en partes compuestas.

    :param image_href: href de una imagen
    :returns: una tupla con el formato (image_id, netloc, use_ssl)
    :raises ValueError: Si el enlace no es válido o no puede ser analizado correctamente.
    """
    try:
        parsed_url = urlparse(image_href)
        if not parsed_url.netloc or not parsed_url.path:
            raise ValueError("Invalid image href: missing netloc or path.")
        
        image_id = parsed_url.path.strip('/')
        netloc = parsed_url.netloc
        use_ssl = parsed_url.scheme == 'https'
        
        return image_id, netloc, use_ssl
    except Exception as e:
        raise ValueError(f"Failed to parse image href: {e}")