import requests
from xml.etree import ElementTree as ET

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    # Construct the webfinger URL
    webfinger_url = f"https://{handle.split('@')[1]}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to the webfinger URL
        response = requests.get(webfinger_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Extract relevant information from the XML
        result = {}
        for link in root.findall('{http://webfinger.net/rel/}link'):
            rel = link.get('rel')
            href = link.get('href')
            result[rel] = href
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving webfinger document: {e}")
        return {}
    except ET.ParseError as e:
        print(f"Error parsing webfinger document: {e}")
        return {}