import json
from typing import Dict
from xml.etree import ElementTree as ET

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
            namespace = {'XRD': 'http://docs.oasis-open.org/ns/xri/xrd-1.0'}
            links = root.findall('XRD:Link', namespace)
            result = {}
            for link in links:
                rel = link.get('rel')
                href = link.get('href')
                if rel and href:
                    result[rel] = href
            return result
        except ET.ParseError:
            # If both JSON and XML parsing fail, return an empty dict
            return {}