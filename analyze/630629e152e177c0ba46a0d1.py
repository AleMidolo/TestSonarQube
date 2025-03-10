import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    try:
        # Extract the domain from the handle
        domain = handle.split('@')[-1]
        webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Make the request to retrieve the webfinger document
        response = requests.get(webfinger_url, timeout=5)
        response.raise_for_status()
        
        # Return the content of the webfinger document
        return response.text
    except (requests.RequestException, ValueError):
        # Return None if any error occurs (e.g., network error, invalid handle)
        return None