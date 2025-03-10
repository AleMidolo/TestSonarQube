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
    if not parsed_url.netloc or not parsed_url.path:
        raise ValueError("Invalid image href: missing netloc or path")

    image_id = parsed_url.path.strip('/')
    if not image_id:
        raise ValueError("Invalid image href: missing image ID")

    use_ssl = parsed_url.scheme == 'https'
    return image_id, parsed_url.netloc, use_ssl