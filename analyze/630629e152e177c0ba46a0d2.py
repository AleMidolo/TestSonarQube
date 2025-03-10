import requests
from urllib.parse import urlparse

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera y analiza un documento "webfinger" remoto de Diaspora.

    :arg handle: Identificador remoto a recuperar
    :returns: dict
    """
    # Parse the handle to extract the username and domain
    if '@' not in handle:
        raise ValueError("Invalid handle format. Expected format: user@domain")
    
    username, domain = handle.split('@')
    
    # Construct the webfinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Make the GET request to retrieve the webfinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the JSON response
        webfinger_data = response.json()
        
        return webfinger_data
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to retrieve webfinger document: {e}")