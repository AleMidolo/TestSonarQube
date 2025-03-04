from urllib.parse import urlparse
from typing import Tuple

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    将图像的 href 解析为多个组成部分，导入 urllib。
    
    :param image_href: 图像的 href
    :returns: 一个元组，格式为 (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    if not image_href:
        raise ValueError("Empty image href")
        
    # Parse the URL
    parsed = urlparse(image_href)
    
    # Get netloc
    netloc = parsed.netloc
    if not netloc:
        raise ValueError("Invalid image href - no netloc found")
        
    # Check if using SSL
    use_ssl = parsed.scheme == 'https'
    
    # Get image ID from path
    path_parts = parsed.path.split('/')
    if not path_parts or len(path_parts) < 2:
        raise ValueError("Invalid image href - no image ID found")
    image_id = path_parts[-1]
    
    return (image_id, netloc, use_ssl)