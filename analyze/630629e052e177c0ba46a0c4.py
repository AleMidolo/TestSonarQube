import json
from xml.etree import ElementTree as ET
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).

    Args:
        document (str): The webfinger document in either JSON or XRD format.

    Returns:
        Dict: A dictionary containing the parsed data.
    """
    try:
        # Try to parse as JSON first
        data = json.loads(document)
        return data
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse as XRD
        try:
            root = ET.fromstring(document)
            namespaces = {
                'XRD': 'http://docs.oasis-open.org/ns/xri/xrd-1.0',
                'diaspora': 'https://diaspora.github.io/diaspora_federation/discovery/webfinger.html'
            }
            result = {}
            for link in root.findall('XRD:Link', namespaces):
                rel = link.get('rel')
                href = link.get('href')
                if rel and href:
                    result[rel] = href
            return result
        except ET.ParseError:
            # If both JSON and XML parsing fail, return an empty dict
            return {}