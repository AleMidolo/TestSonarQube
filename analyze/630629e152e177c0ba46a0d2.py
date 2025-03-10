import requests
from urllib.parse import urlparse
from lxml import etree

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
        
        # Parse the XML response
        root = etree.fromstring(response.content)
        
        # Extract relevant information from the XML
        result = {}
        for link in root.findall('{http://webfinger.net/rel/profile-page}link'):
            result['profile_page'] = link.get('href')
        
        for link in root.findall('{http://webfinger.net/rel/avatar}link'):
            result['avatar'] = link.get('href')
        
        for link in root.findall('{http://webfinger.net/rel/hcard}link'):
            result['hcard'] = link.get('href')
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving webfinger document: {e}")
        return {}
    except etree.XMLSyntaxError as e:
        print(f"Error parsing webfinger document: {e}")
        return {}