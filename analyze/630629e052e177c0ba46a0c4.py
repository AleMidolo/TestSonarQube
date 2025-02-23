from typing import Dict
import json
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Analizza il webfinger di Diaspora, che può essere in formato JSON (nuovo) o in formato XRD (vecchio).

    [https://diaspora.github.io/diaspora_federation/discovery/webfinger.html](https://diaspora.github.io/diaspora_federation/discovery/webfinger.html)
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