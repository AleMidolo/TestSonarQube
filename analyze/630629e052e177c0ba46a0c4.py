import json
from typing import Dict
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    डायस्पोरा वेबफिंगर को पार्स करें, जो या तो JSON प्रारूप (नया) में होता है या XRD (पुराना) में।  

    [डायस्पोरा वेबफिंगर के बारे में अधिक जानकारी के लिए यहां क्लिक करें।](https://diaspora.github.io/diaspora_federation/discovery/webfinger.html)
    """
    try:
        # Try to parse the document as JSON
        return json.loads(document)
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse as XRD (XML)
        root = ET.fromstring(document)
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result