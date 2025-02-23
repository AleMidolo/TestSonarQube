from typing import Dict
import json
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    try:
        # Try to parse as JSON
        return json.loads(document)
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse as XRD (XML)
        root = ET.fromstring(document)
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result