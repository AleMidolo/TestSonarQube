import json
from xml.etree import ElementTree as ET
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
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
            for child in root:
                if child.tag.endswith('Link'):
                    rel = child.attrib.get('rel')
                    href = child.attrib.get('href')
                    if rel and href:
                        result[rel] = href
                elif child.tag.endswith('Subject'):
                    result['subject'] = child.text
            return result
        except ET.ParseError:
            # If both JSON and XML parsing fail, return an empty dict
            return {}