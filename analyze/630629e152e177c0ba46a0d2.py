import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Construct the webfinger URL
    webfinger_url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
    
    # Send a GET request to the webfinger URL
    response = requests.get(webfinger_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()
    else:
        # Handle errors (e.g., return an empty dict or raise an exception)
        return {}