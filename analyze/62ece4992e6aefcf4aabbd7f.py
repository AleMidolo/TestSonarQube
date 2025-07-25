def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    from urllib.parse import urlparse
    
    try:
        # Parse the URL into components
        parsed = urlparse(image_href)
        
        # Get the netloc (domain)
        netloc = parsed.netloc
        
        # Determine if SSL should be used based on scheme
        use_ssl = parsed.scheme == 'https'
        
        # Extract image ID from path
        path_parts = parsed.path.strip('/').split('/')
        if not path_parts or not path_parts[-1]:
            raise ValueError("Invalid image reference - missing image ID")
            
        image_id = path_parts[-1]
        
        # Validate components
        if not netloc or not image_id:
            raise ValueError("Invalid image reference - missing required components")
            
        return (image_id, netloc, use_ssl)
        
    except Exception as e:
        raise ValueError(f"Invalid image reference: {str(e)}")