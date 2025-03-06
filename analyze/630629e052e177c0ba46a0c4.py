import json
from xml.etree import ElementTree as ET
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Analizza il webfinger di Diaspora, che può essere in formato JSON (nuovo) o in formato XRD (vecchio).

    [https://diaspora.github.io/diaspora_federation/discovery/webfinger.html](https://diaspora.github.io/diaspora_federation/discovery/webfinger.html)
    """
    try:
        # Try to parse as JSON (new format)
        data = json.loads(document)
        return data
    except json.JSONDecodeError:
        # If JSON parsing fails, try to parse as XML (old format)
        try:
            root = ET.fromstring(document)
            namespace = {'XRD': 'http://docs.oasis-open.org/ns/xri/xrd-1.0'}
            links = root.findall('XRD:Link', namespace)
            result = {
                'subject': root.find('XRD:Subject', namespace).text,
                'aliases': [alias.text for alias in root.findall('XRD:Alias', namespace)],
                'links': []
            }
            for link in links:
                link_data = {
                    'rel': link.attrib.get('rel'),
                    'type': link.attrib.get('type'),
                    'href': link.attrib.get('href'),
                    'template': link.attrib.get('template')
                }
                result['links'].append(link_data)
            return result
        except ET.ParseError:
            raise ValueError("Invalid document format. Expected JSON or XRD XML.")