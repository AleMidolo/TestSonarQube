import requests
from urllib.parse import urlparse
from lxml import etree

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Recupera e analizza un documento webfinger remoto di Diaspora.

    :arg handle: Handle remoto da recuperare  
    :returns: dict
    """
    # Parse the handle to extract the username and domain
    username, domain = handle.split('@')
    
    # Construct the WebFinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to the WebFinger URL
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the XML response
        root = etree.fromstring(response.content)
        
        # Extract relevant information from the XML
        result = {}
        for link in root.findall("{http://webfinger.net/rel/profile-page}link"):
            result[link.get("rel")] = link.get("href")
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving WebFinger document: {e}")
        return {}
    except etree.XMLSyntaxError as e:
        print(f"Error parsing WebFinger document: {e}")
        return {}