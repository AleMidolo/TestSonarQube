import requests
from urllib.parse import urlparse

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera y analiza un documento "webfinger" remoto de Diaspora.

    :arg handle: Identificador remoto a recuperar
    :returns: dict
    """
    # Parse the handle to extract the username and domain
    if not handle.startswith('acct:'):
        handle = 'acct:' + handle
    username, domain = handle.split('@')[1], handle.split('@')[2]

    # Construct the webfinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource={handle}"

    try:
        # Make the GET request to retrieve the webfinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        webfinger_data = response.json()

        return webfinger_data

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving webfinger document: {e}")
        return {}