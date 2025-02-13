import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    Recupera l'intestazione HEAD dell'URL remoto per determinare il tipo di contenuto.
    """
    try:
        response = requests.head(url)
        return response.headers.get('Content-Type')
    except requests.RequestException:
        return None