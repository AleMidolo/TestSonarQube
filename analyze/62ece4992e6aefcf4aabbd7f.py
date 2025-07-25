from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizar un enlace (href) de una imagen en partes compuestas.

    :param image_href: href de una imagen
    :returns: una tupla con el formato (image_id, netloc, use_ssl)
    :raises ValueError: 

    Explicación de los parámetros y retorno:
    - `image_href`: href de una imagen.
    - Retorno: una tupla con el formato `(image_id, netloc, use_ssl)`, donde:
      - `image_id`: Identificador unico de la imagen.
      - `netloc`: Localizacion de la red (dominio o dirección base del enlace).
      - `use_ssl`: Un valor booleano que indica si se utiliza SSL (https).

    Excepcion:
    - `ValueError`: Se lanza si el enlace no es valido o no puede ser analizado correctamente.
    """
    parsed_url = urlparse(image_href)
    
    if not all([parsed_url.scheme, parsed_url.netloc, parsed_url.path]):
        raise ValueError("El enlace proporcionado no es válido.")
    
    image_id = parsed_url.path.split('/')[-1]  # Asumiendo que el ID de la imagen es el último segmento del path
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'
    
    return image_id, netloc, use_ssl