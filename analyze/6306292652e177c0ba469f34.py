import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.head(url, headers=headers)
        return response.headers.get('Content-Type')
    except requests.RequestException:
        return None