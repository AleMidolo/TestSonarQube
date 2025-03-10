import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    Prova a recuperare un documento webfinger conforme a RFC7033. Non genera eccezioni in caso di fallimento.
    """
    try:
        # Split the handle into username and domain
        username, domain = handle.split('@')
        
        # Construct the WebFinger URL
        url = f"https://{domain}/.well-known/webfinger?resource=acct:{username}@{domain}"
        
        # Make the GET request
        response = requests.get(url, headers={"Accept": "application/jrd+json"})
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None