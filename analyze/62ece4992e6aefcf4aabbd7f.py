from urllib.parse import urlparse

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizza un href di un'immagine in parti composite.

    :param image_href: href di un'immagine
    :returns: una tupla nella forma (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    parsed_url = urlparse(image_href)
    
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid image href")

    image_id = parsed_url.path.lstrip('/')
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'

    return image_id, netloc, use_ssl