def parse_diaspora_webfinger(document: str) -> Dict:
    """
    डायस्पोरा वेबफिंगर को पार्स करें, जो या तो JSON प्रारूप (नया) में होता है या XRD (पुराना) में।
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
            result['links'].append({
                'rel': link.get('rel', ''),
                'type': link.get('type', ''),
                'href': link.get('href', '')
            })
            
        return result

    except json.JSONDecodeError:
        # If JSON parsing fails, try XRD format
        try:
            # Remove XML namespace to simplify parsing
            document = document.replace('xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0"', '')
            root = ET.fromstring(document)
            
            result = {
                'subject': '',
                'aliases': [],
                'links': []
            }
            
            # Get subject
            subject = root.find('Subject')
            if subject is not None:
                result['subject'] = subject.text
                
            # Get aliases
            for alias in root.findall('Alias'):
                if alias.text:
                    result['aliases'].append(alias.text)
                    
            # Get links
            for link in root.findall('Link'):
                link_data = {
                    'rel': link.get('rel', ''),
                    'type': link.get('type', ''),
                    'href': link.get('href', '')
                }
                result['links'].append(link_data)
                
            return result
            
        except ET.ParseError:
            raise ValueError("Invalid document format - neither valid JSON nor XRD")

    return {}