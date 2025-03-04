def retrieve_and_parse_diaspora_webfinger(handle):
    """
    डायस्पोरा वेबफिंगर डॉक्यूमेंट को प्राप्त करें और पार्स करें।

    :पैरामीटर हैंडल: प्राप्त करने के लिए रिमोट हैंडल  
    :वापसी: डिक्शनरी (dict)
    """
    import requests
    import json
    from urllib.parse import urlparse

    # Handle validation
    if '@' not in handle:
        raise ValueError("Invalid handle format - must contain @")

    # Split handle into user and domain
    username, domain = handle.split('@', 1)
    
    # Construct webfinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger"
    params = {
        'resource': f'acct:{handle}'
    }

    try:
        # Make request to webfinger endpoint
        response = requests.get(webfinger_url, params=params)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract relevant information
        result = {
            'handle': handle,
            'domain': domain,
            'username': username,
            'links': {}
        }
        
        # Parse links
        if 'links' in data:
            for link in data['links']:
                if 'rel' in link:
                    result['links'][link['rel']] = {
                        'href': link.get('href', ''),
                        'type': link.get('type', '')
                    }
                    
        return result

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to retrieve webfinger document: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Invalid webfinger document format")
    except Exception as e:
        raise Exception(f"Error processing webfinger document: {str(e)}")