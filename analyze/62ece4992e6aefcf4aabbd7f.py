from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    छवि के हाइपरलिंक (href) को उसके घटक भागों में विभाजित करें।

    :param image_href: छवि का हाइपरलिंक (href)
    :returns: एक ट्यूपल (tuple) के रूप में परिणाम, जिसमें (image_id, netloc, use_ssl) शामिल हैं
    :raises ValueError: यदि हाइपरलिंक अमान्य है
    """
    parsed_url = urlparse(image_href)
    
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise ValueError("अमान्य हाइपरलिंक")

    image_id = parsed_url.path.lstrip('/')
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'

    return image_id, netloc, use_ssl