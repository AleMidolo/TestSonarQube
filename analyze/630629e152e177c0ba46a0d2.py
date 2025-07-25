import requests

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    检索并解析远程 Diaspora WebFinger 文档。

    :arg handle: 要检索的远程句柄
    :returns: 字典
    """
    # Construct the WebFinger URL
    webfinger_url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to the WebFinger URL
        response = requests.get(webfinger_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        webfinger_data = response.json()
        
        return webfinger_data
    except requests.RequestException as e:
        print(f"Error retrieving WebFinger document: {e}")
        return {}
    except ValueError as e:
        print(f"Error parsing WebFinger document: {e}")
        return {}