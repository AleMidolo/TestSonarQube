import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    base_url = f"https://{handle.split('@')[1]}/.well-known/webfinger?resource=acct:{handle}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()