from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    url = f"https://webfinger.example.com/.well-known/webfinger?resource=acct:{handle}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None