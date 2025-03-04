def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    import requests
    from urllib.parse import urlparse, quote
    
    try:
        # Split handle into user and domain
        if '@' not in handle:
            return None
            
        user, domain = handle.split('@', 1)
        
        # Construct webfinger URL
        webfinger_url = f"https://{domain}/.well-known/webfinger"
        params = {
            'resource': f'acct:{quote(user)}@{domain}'
        }
        
        # Make request
        response = requests.get(webfinger_url, params=params, timeout=10)
        
        if response.status_code == 200:
            return response.text
            
    except (requests.RequestException, ValueError):
        pass
        
    return None