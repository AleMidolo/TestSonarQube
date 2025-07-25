from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError: if the image_href is not a valid URL or does not contain an image ID
    """
    parsed_url = urlparse(image_href)
    if not parsed_url.netloc:
        raise ValueError("Invalid image href: no netloc found")
    
    path_parts = parsed_url.path.strip('/').split('/')
    if not path_parts:
        raise ValueError("Invalid image href: no image ID found")
    
    image_id = path_parts[-1]
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'
    
    return image_id, netloc, use_ssl