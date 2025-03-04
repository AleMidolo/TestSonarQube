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
    
    # Check if scheme is http or https
    if parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")
        
    # Get the netloc (hostname)
    netloc = parsed.netloc
    if not netloc:
        raise ValueError("Missing hostname in URL")
        
    # Extract image ID from path
    path_parts = parsed.path.strip('/').split('/')
    if not path_parts or not path_parts[-1]:
        raise ValueError("Missing image ID in URL")
    image_id = path_parts[-1]
    
    # Determine if using SSL
    use_ssl = parsed.scheme == 'https'
    
    return (image_id, netloc, use_ssl)