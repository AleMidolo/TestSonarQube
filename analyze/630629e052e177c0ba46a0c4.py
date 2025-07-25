def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).
    """
    import json
    from xml.etree import ElementTree as ET
    
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
            # Add XML namespace
            ns = {'xrd': 'http://docs.oasis-open.org/ns/xri/xrd-1.0'}
            
            root = ET.fromstring(document)
            result = {
                'subject': '',
                'aliases': [],
                'links': []
            }
            
            # Get subject
            subject = root.find('xrd:Subject', ns)
            if subject is not None:
                result['subject'] = subject.text
                
            # Get aliases
            for alias in root.findall('xrd:Alias', ns):
                if alias.text:
                    result['aliases'].append(alias.text)
                    
            # Get links
            for link in root.findall('xrd:Link', ns):
                link_data = {
                    'rel': link.get('rel', ''),
                    'type': link.get('type', ''),
                    'href': link.get('href', '')
                }
                result['links'].append(link_data)
                
            return result
            
        except ET.ParseError:
            raise ValueError("Invalid webfinger document format")
            
    return {}