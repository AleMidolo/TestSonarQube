import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    Obtén el encabezado HEAD de la URL remota para determinar el tipo de contenido.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        return content_type
    except requests.RequestException:
        return None