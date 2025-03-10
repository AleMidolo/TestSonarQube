import requests
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Split the handle into username and domain
    username, domain = handle.split('@')
    
    # Construct the webfinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to the webfinger URL
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Extract relevant information
        result = {}
        for link in root.findall('{http://webfinger.net/rel/profile-page}link'):
            if link.get('rel') == 'http://webfinger.net/rel/profile-page':
                result['profile_page'] = link.get('href')
            elif link.get('rel') == 'http://webfinger.net/rel/avatar':
                result['avatar'] = link.get('href')
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving webfinger document: {e}")
        return {}
    except ET.ParseError as e:
        print(f"Error parsing webfinger document: {e}")
        return {}