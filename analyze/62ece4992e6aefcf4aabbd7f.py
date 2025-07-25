from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    将图像的 href 解析为多个组成部分，导入 urllib。
    
    :param image_href: 图像的 href
    :returns: 一个元组，格式为 (image_id, netloc, use_ssl)
    :raises ValueError:

    将图像的 href 解析为多个组成部分
    """
    parsed_url = urlparse(image_href)
    
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid image href provided.")
    
    image_id = parsed_url.path.lstrip('/')
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'
    
    return image_id, netloc, use_ssl