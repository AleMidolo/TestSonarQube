from typing import Dict
import json
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Analiza el webfinger de Diaspora, que puede estar en formato JSON (nuevo) o en formato XRD (antiguo).

    [https://diaspora.github.io/diaspora_federation/discovery/webfinger.html](https://diaspora.github.io/diaspora_federation/discovery/webfinger.html)
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