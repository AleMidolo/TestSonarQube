import json
from xml.etree import ElementTree as ET
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Analiza el webfinger de Diaspora, que puede estar en formato JSON (nuevo) o en formato XRD (antiguo).

    Args:
        document (str): El documento webfinger en formato JSON o XRD.

    Returns:
        Dict: Un diccionario con la información extraída del webfinger.
    """
    try:
        # Intentar parsear como JSON
        data = json.loads(document)
        return data
    except json.JSONDecodeError:
        # Si falla, intentar parsear como XML (XRD)
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
            # Si no es ni JSON ni XML válido, devolver un diccionario vacío
            return {}