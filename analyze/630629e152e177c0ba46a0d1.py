def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Intenta recuperar un documento webfinger conforme a RFC7033.
    No genera una excepción si falla.
    """
    import requests
    from urllib.parse import urlparse, quote
    from typing import Optional

    try:
        # Validar formato del handle
        if '@' not in handle:
            return None
            
        # Separar usuario y dominio
        user, domain = handle.split('@', 1)
        
        # Construir URL webfinger según RFC7033
        webfinger_url = f"https://{domain}/.well-known/webfinger"
        params = {
            'resource': f'acct:{quote(user)}@{domain}'
        }

        # Realizar petición HTTP
        response = requests.get(webfinger_url, params=params, timeout=10)
        
        if response.status_code == 200:
            return response.text
        else:
            return None
            
    except Exception:
        # Capturar cualquier error y retornar None
        return None