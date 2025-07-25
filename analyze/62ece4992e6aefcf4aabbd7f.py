def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    छवि के हाइपरलिंक (href) को उसके घटक भागों में विभाजित करें।

    :param image_href: छवि का हाइपरलिंक (href)
    :returns: एक ट्यूपल (tuple) के रूप में परिणाम, जिसमें (image_id, netloc, use_ssl) शामिल हैं
    :raises ValueError: यदि हाइपरलिंक अमान्य है
    """
    from urllib.parse import urlparse

    try:
        # Parse the URL
        parsed = urlparse(image_href)
        
        # Check if scheme is http or https
        if parsed.scheme not in ['http', 'https']:
            raise ValueError("Invalid URL scheme")
            
        # Determine if SSL is used
        use_ssl = parsed.scheme == 'https'
        
        # Get the netloc (hostname)
        netloc = parsed.netloc
        
        # Extract image ID from path
        path_parts = parsed.path.strip('/').split('/')
        if not path_parts or not path_parts[-1]:
            raise ValueError("Invalid image path")
            
        image_id = path_parts[-1]
        
        return (image_id, netloc, use_ssl)
        
    except Exception as e:
        raise ValueError(f"Invalid image URL: {str(e)}")