import requests
from lxml import etree

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    डायस्पोरा वेबफिंगर डॉक्यूमेंट को प्राप्त करें और पार्स करें।

    :पैरामीटर हैंडल: प्राप्त करने के लिए रिमोट हैंडल  
    :वापसी: डिक्शनरी (dict)
    """
    # Construct the WebFinger URL
    webfinger_url = f"https://{handle.split('@')[1]}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # Send a GET request to retrieve the WebFinger document
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # Parse the XML response
        root = etree.fromstring(response.content)
        
        # Extract relevant information into a dictionary
        result = {}
        for link in root.findall("{http://webfinger.net/rel/}link"):
            rel = link.get("rel")
            href = link.get("href")
            result[rel] = href
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving WebFinger document: {e}")
        return {}
    except etree.XMLSyntaxError as e:
        print(f"Error parsing WebFinger document: {e}")
        return {}