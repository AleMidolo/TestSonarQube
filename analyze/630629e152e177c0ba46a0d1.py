import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Prova a recuperare un documento webfinger conforme a RFC7033. Non genera eccezioni in caso di fallimento.
    """
    try:
        # Extract the domain from the handle
        domain = handle.split('@')[-1]
        webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Make the request to retrieve the WebFinger document
        response = requests.get(webfinger_url, timeout=5)
        response.raise_for_status()
        
        # Return the document if successful
        return response.text
    except (requests.RequestException, IndexError):
        # Return None in case of any failure
        return None