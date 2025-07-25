import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    Fetch the HEAD of the remote url to determine the content type.
    """
    try:
        response = requests.head(url)
        response.raise_for_status()
        return response.headers.get('Content-Type')
    except requests.RequestException:
        return None