def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    将图像的 href 解析为多个组成部分，导入 urllib。
    
    :param image_href: 图像的 href
    :returns: 一个元组，格式为 (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    from urllib.parse import urlparse

    if not image_href:
        raise ValueError("Empty image href")

    # Parse the URL
    parsed = urlparse(image_href)
    
    # Get netloc (domain)
    netloc = parsed.netloc
    if not netloc:
        raise ValueError("Invalid image href: missing domain")

    # Determine if using SSL
    use_ssl = parsed.scheme == 'https'

    # Extract image ID from path
    path_parts = parsed.path.split('/')
    if len(path_parts) < 2:
        raise ValueError("Invalid image href: missing image ID")
    image_id = path_parts[-1]  # Get last part of path as image ID
    
    if not image_id:
        raise ValueError("Invalid image href: empty image ID")

    return (image_id, netloc, use_ssl)