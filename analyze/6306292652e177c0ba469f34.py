import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    Obtén el encabezado HEAD de la URL remota para determinar el tipo de contenido.
    """
    try:
        response = requests.head(url)
        return response.headers.get('Content-Type')
    except requests.RequestException:
        return None