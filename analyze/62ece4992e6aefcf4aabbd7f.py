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

    # Get the netloc (hostname)
    netloc = parsed.netloc
    if not netloc:
        raise ValueError(f"No hostname found in URL: {image_href}")

    # Determine if SSL should be used
    use_ssl = parsed.scheme == 'https'

    # Extract image ID from path
    path_parts = parsed.path.split('/')
    image_id = path_parts[-1] if path_parts else ''
    
    if not image_id:
        raise ValueError(f"No image ID found in URL: {image_href}")

    return (image_id, netloc, use_ssl)