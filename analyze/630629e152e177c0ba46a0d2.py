import requests
from urllib.parse import urlparse

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    # Split the handle into username and domain
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
        # Handle any errors that occur during the request
        print(f"Error retrieving webfinger document: {e}")
        return {}