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
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None