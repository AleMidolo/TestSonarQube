def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Analizza un href di un'immagine in parti composite.

    :param image_href: href di un'immagine 
    :returns: una tupla nella forma (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    from urllib.parse import urlparse
    
    if not image_href:
        raise ValueError("Empty image href")
        
    # Parse the URL
    parsed = urlparse(image_href)
    
    # Check if scheme is http/https
    if parsed.scheme not in ('http', 'https', ''):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")
        
    # Get netloc, default to empty string if not present
    netloc = parsed.netloc if parsed.netloc else ''
    
    # Determine if SSL should be used
    use_ssl = parsed.scheme == 'https'
    
    # Extract image ID from path
    path_parts = parsed.path.strip('/').split('/')
    if not path_parts or not path_parts[-1]:
        raise ValueError("No image ID found in URL")
        
    image_id = path_parts[-1]
    
    return (image_id, netloc, use_ssl)