import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Intenta recuperar un documento webfinger conforme a RFC7033. 
    No genera una excepción si falla.
    """
    try:
        # Parse the handle to extract the domain
        if '@' not in handle:
            return None
        username, domain = handle.split('@')
        
        # Construct the WebFinger URL
        url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Make the request
        response = requests.get(url, headers={"Accept": "application/jrd+json"})
        response.raise_for_status()
        
        # Return the response content if successful
        return response.text
    except (requests.RequestException, ValueError):
        # Return None if any error occurs
        return None