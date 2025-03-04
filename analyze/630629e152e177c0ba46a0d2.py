def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    import requests
    import xml.etree.ElementTree as ET
    from urllib.parse import urlparse

    # Split handle into user and host
    if '@' not in handle:
        raise ValueError("Handle must contain @")
    
    username, host = handle.split('@', 1)
    
    # Construct webfinger URL
    webfinger_url = f"https://{host}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Get the webfinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the response
        data = response.json()
        
        # Extract relevant information into a dict
        result = {
            'handle': handle,
            'host': host,
            'username': username,
            'links': {}
        }
        
        # Parse links
        for link in data.get('links', []):
            rel = link.get('rel', '')
            if rel:
                result['links'][rel] = {
                    'href': link.get('href', ''),
                    'type': link.get('type', '')
                }
                
        # Add additional properties if they exist
        if 'aliases' in data:
            result['aliases'] = data['aliases']
        if 'subject' in data:
            result['subject'] = data['subject']
            
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to retrieve webfinger document: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Failed to parse webfinger document: {str(e)}")