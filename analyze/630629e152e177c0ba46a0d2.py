import requests
from xml.etree import ElementTree as ET

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Construct the webfinger URL
    domain = handle.split('@')[-1]
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to retrieve the webfinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Extract relevant information
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
    except ET.ParseError as e:
        print(f"Error parsing webfinger document: {e}")
        return {}