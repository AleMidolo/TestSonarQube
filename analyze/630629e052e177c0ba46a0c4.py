def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Analiza el webfinger de Diaspora, que puede estar en formato JSON (nuevo) o en formato XRD (antiguo).
    
    Args:
        document: String containing the webfinger document in JSON or XRD format
        
    Returns:
        Dictionary with parsed webfinger data
    """
    import json
    import xml.etree.ElementTree as ET
    from typing import Dict
    
    # Try parsing as JSON first
    try:
        data = json.loads(document)
        result = {
            'subject': data.get('subject', ''),
            'aliases': data.get('aliases', []),
            'links': []
        }
        
        # Parse links
        for link in data.get('links', []):
            link_data = {
                'rel': link.get('rel', ''),
                'href': link.get('href', ''),
                'type': link.get('type', '')
            }
            result['links'].append(link_data)
            
        return result
        
    except json.JSONDecodeError:
        # If JSON fails, try parsing as XRD
        try:
            # Remove XML namespace to simplify parsing
            document = document.replace('xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0"', '')
            root = ET.fromstring(document)
            
            result = {
                'subject': root.find('Subject').text if root.find('Subject') is not None else '',
                'aliases': [alias.text for alias in root.findall('Alias')],
                'links': []
            }
            
            # Parse links
            for link in root.findall('Link'):
                link_data = {
                    'rel': link.get('rel', ''),
                    'href': link.get('href', ''),
                    'type': link.get('type', '')
                }
                result['links'].append(link_data)
                
            return result
            
        except ET.ParseError:
            raise ValueError("Invalid webfinger document format - neither JSON nor XRD")