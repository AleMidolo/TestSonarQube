import json
from xml.etree import ElementTree as ET
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    डायस्पोरा वेबफिंगर को पार्स करें, जो या तो JSON प्रारूप (नया) में होता है या XRD (पुराना) में।  

    [डायस्पोरा वेबफिंगर के बारे में अधिक जानकारी के लिए यहां क्लिक करें।](https://diaspora.github.io/diaspora_federation/discovery/webfinger.html)
    """
    try:
        # Try to parse as JSON (new format)
        data = json.loads(document)
        return data
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse as XML (XRD format)
        try:
            root = ET.fromstring(document)
            result = {}
            for link in root.findall('{http://docs.oasis-open.org/ns/xri/xrd-1.0}Link'):
                rel = link.get('rel')
                href = link.get('href')
                if rel and href:
                    result[rel] = href
            return result
        except ET.ParseError:
            # If both JSON and XML parsing fail, return an empty dict
            return {}