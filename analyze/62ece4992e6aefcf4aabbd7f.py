def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts.

    :param image_href: href of an image 
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    if not image_href:
        raise ValueError("Image href cannot be empty")
        
    # Try to parse the URL
    try:
        parsed = urllib.parse.urlparse(image_href)
    except Exception:
        raise ValueError(f"Invalid URL format: {image_href}")

    # Get netloc
    netloc = parsed.netloc
    if not netloc:
        raise ValueError(f"No host specified in href: {image_href}")

    # Determine if SSL should be used
    use_ssl = parsed.scheme == 'https'

    # Extract image ID from path
    path_parts = parsed.path.split('/')
    if not path_parts or len(path_parts) < 2:
        raise ValueError(f"No image ID found in href: {image_href}")
    
    # Get last non-empty part as image ID
    image_id = next((p for p in reversed(path_parts) if p), None)
    if not image_id:
        raise ValueError(f"No image ID found in href: {image_href}")

    return (image_id, netloc, use_ssl)