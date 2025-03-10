from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Intenta recuperar un documento webfinger conforme a RFC7033. 
    No genera una excepción si falla.
    """
    try:
        # Parse the handle to extract the domain
        if '@' not in handle:
            return None
        username, domain = handle.split('@', 1)
        
        # Construct the webfinger URL
        webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Make the request
        response = requests.get(webfinger_url, timeout=5)
        response.raise_for_status()
        
        # Return the response content if successful
        return response.text
    except (requests.RequestException, ValueError):
        # Return None if any error occurs
        return None