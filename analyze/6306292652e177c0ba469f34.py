def fetch_content_type(url: str) -> Optional[str]:
    """
    Recupera l'intestazione HEAD dell'URL remoto per determinare il tipo di contenuto.
    """
    import requests
    from typing import Optional
    
    try:
        # Effettua una richiesta HEAD per ottenere solo le intestazioni
        response = requests.head(url, allow_redirects=True)
        
        # Verifica se la richiesta ha avuto successo
        if response.status_code == 200:
            # Restituisce il content-type dalle intestazioni
            return response.headers.get('content-type')
        
        return None
        
    except requests.RequestException:
        # In caso di errori nella richiesta, restituisce None
        return None