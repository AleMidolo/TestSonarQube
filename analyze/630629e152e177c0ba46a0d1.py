def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Prova a recuperare un documento webfinger conforme a RFC7033. Non genera eccezioni in caso di fallimento.
    """
    import requests
    from urllib.parse import urlparse, quote
    from typing import Optional

    try:
        # Split handle into user and domain
        if '@' not in handle:
            return None
            
        user, domain = handle.split('@')
        
        # Construct webfinger URL according to RFC7033
        resource = f'acct:{quote(user)}@{domain}'
        webfinger_url = f'https://{domain}/.well-known/webfinger?resource={resource}'
        
        # Make request with timeout
        response = requests.get(webfinger_url, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.text
            
    except (requests.RequestException, ValueError):
        pass
        
    return None