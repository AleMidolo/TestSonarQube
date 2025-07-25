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
    
    user, host = handle.split('@', 1)
    
    # Construct webfinger URL
    webfinger_url = f"https://{host}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Get the webfinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant information
        result = {
            'handle': handle,
            'host': host,
            'guid': None,
            'profile_url': None,
            'atom_url': None,
            'salmon_url': None,
            'pubkey': None
        }
        
        # Parse links
        for link in data.get('links', []):
            rel = link.get('rel', '')
            href = link.get('href', '')
            
            if rel == 'http://microformats.org/profile/hcard':
                result['profile_url'] = href
            elif rel == 'http://schemas.google.com/g/2010#updates-from':
                result['atom_url'] = href
            elif rel == 'salmon':
                result['salmon_url'] = href
                
        # Get additional properties
        for prop in data.get('properties', {}):
            if prop == 'http://joindiaspora.com/guid':
                result['guid'] = data['properties'][prop]
            elif prop == 'http://joindiaspora.com/seed_location':
                result['pod'] = data['properties'][prop]
                
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to retrieve webfinger document: {str(e)}")
    except (ValueError, KeyError) as e:
        raise ValueError(f"Failed to parse webfinger document: {str(e)}")