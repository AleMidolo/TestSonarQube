from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Intenta recuperar un documento webfinger conforme a RFC7033. 
    No genera una excepción si falla.
    """
    try:
        url = f"https://webfinger.example.com/whois/{handle}"
        response = requests.get(url, params={'resource': f"acct:{handle}"})
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None