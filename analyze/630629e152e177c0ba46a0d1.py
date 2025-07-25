import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
    """
    try:
        # Split the handle into username and domain
        username, domain = handle.split('@')
        
        # Construct the webfinger URL
        url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        # Make the GET request
        response = requests.get(url, headers={"Accept": "application/jrd+json"})
        response.raise_for_status()
        
        # Return the response content if successful
        return response.text
    except Exception:
        # Return None if any error occurs
        return None