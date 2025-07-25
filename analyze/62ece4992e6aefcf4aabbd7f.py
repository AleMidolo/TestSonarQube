def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    from urllib.parse import urlparse
    
    try:
        # Parse the URL into components
        parsed = urlparse(image_href)
        
        # Check if scheme is valid (http or https)
        if parsed.scheme not in ('http', 'https', ''):
            raise ValueError("Invalid URL scheme")
            
        # Get the netloc (domain)
        netloc = parsed.netloc
        if not netloc:
            raise ValueError("Missing domain in URL")
            
        # Extract image ID from path
        path_parts = parsed.path.strip('/').split('/')
        if not path_parts or not path_parts[-1]:
            raise ValueError("Invalid image path")
        image_id = path_parts[-1]
        
        # Determine if SSL should be used
        use_ssl = parsed.scheme == 'https'
        
        return (image_id, netloc, use_ssl)
        
    except Exception as e:
        raise ValueError(f"Invalid image URL: {str(e)}")