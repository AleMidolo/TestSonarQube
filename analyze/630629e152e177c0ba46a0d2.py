import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    # Construct the webfinger URL
    webfinger_url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
    
    # Send a GET request to the webfinger URL
    response = requests.get(webfinger_url)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()
    else:
        # Handle errors (e.g., return an empty dict or raise an exception)
        return {}