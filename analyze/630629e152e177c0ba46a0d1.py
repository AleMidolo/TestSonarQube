import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    try:
        response = requests.get(f"https://webfinger.example.com/.well-known/webfinger?resource=acct:{handle}")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None