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
            # Parse XML
            root = ET.fromstring(document)
            
            # Define XML namespaces
            ns = {
                'xrd': 'http://docs.oasis-open.org/ns/xri/xrd-1.0',
                'hm': 'http://host-meta.net/xrd/1.0'
            }
            
            result = {
                'subject': '',
                'aliases': [],
                'links': []
            }
            
            # Get subject
            subject = root.find('.//xrd:Subject', ns)
            if subject is not None:
                result['subject'] = subject.text
                
            # Get aliases
            for alias in root.findall('.//xrd:Alias', ns):
                if alias.text:
                    result['aliases'].append(alias.text)
                    
            # Get links
            for link in root.findall('.//xrd:Link', ns):
                link_data = {
                    'rel': link.get('rel', ''),
                    'href': link.get('href', ''),
                    'type': link.get('type', '')
                }
                result['links'].append(link_data)
                
            return result
            
        except ET.ParseError:
            raise ValueError("Document is neither valid JSON nor valid XRD XML")
            
    return {}