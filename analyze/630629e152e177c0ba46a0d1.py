def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Prova a recuperare un documento webfinger conforme a RFC7033. Non genera eccezioni in caso di fallimento.
    """
    import requests
    from urllib.parse import urlparse, quote
    from typing import Optional

    try:
        # Verifica che l'handle sia nel formato corretto (user@domain)
        if '@' not in handle:
            return None
            
        username, domain = handle.split('@')
        
        # Costruisci l'URL del documento webfinger
        webfinger_url = f"https://{domain}/.well-known/webfinger"
        params = {
            'resource': f'acct:{quote(handle)}'
        }
        
        # Effettua la richiesta HTTP
        response = requests.get(
            webfinger_url,
            params=params,
            headers={'Accept': 'application/jrd+json'},
            timeout=10
        )
        
        # Verifica il codice di stato
        if response.status_code == 200:
            return response.text
            
    except (requests.RequestException, ValueError):
        pass
        
    return None