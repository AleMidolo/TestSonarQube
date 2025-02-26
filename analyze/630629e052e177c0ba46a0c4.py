from typing import Dict
import json
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    try:
        # Try to parse the document as JSON
        data = json.loads(document)
        return data
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse it as XRD (XML)
        root = ET.fromstring(document)
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result