def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image 
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    from urllib.parse import urlparse
    
    if not image_href:
        raise ValueError("Image href cannot be empty")
        
    # Try to parse the URL
    try:
        parsed = urlparse(image_href)
    except Exception:
        raise ValueError(f"Invalid image href: {image_href}")
        
    # Get the netloc (hostname)
    netloc = parsed.netloc
    if not netloc:
        raise ValueError(f"No hostname found in href: {image_href}")
        
    # Determine if using SSL based on scheme
    use_ssl = parsed.scheme == 'https'
    
    # Get image ID from path
    path_parts = parsed.path.split('/')
    image_id = path_parts[-1] if path_parts else ''
    
    if not image_id:
        raise ValueError(f"No image ID found in href: {image_href}")
        
    return (image_id, netloc, use_ssl)