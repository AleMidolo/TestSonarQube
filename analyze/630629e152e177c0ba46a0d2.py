import requests
from lxml import etree

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    检索并解析远程 Diaspora WebFinger 文档。

    :arg handle: 要检索的远程句柄
    :returns: 字典
    """
    # Construct the WebFinger URL
    webfinger_url = f"https://{handle.split('@')[1]}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to the WebFinger URL
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the XML response
        root = etree.fromstring(response.content)
        
        # Extract relevant information from the XML
        result = {}
        for link in root.findall("{http://webfinger.net/rel/profile-page}"):
            result['profile_page'] = link.get('href')
        
        for link in root.findall("{http://webfinger.net/rel/avatar}"):
            result['avatar'] = link.get('href')
        
        for link in root.findall("{http://webfinger.net/rel/hcard}"):
            result['hcard'] = link.get('href')
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving WebFinger document: {e}")
        return {}
    except etree.XMLSyntaxError as e:
        print(f"Error parsing WebFinger document: {e}")
        return {}