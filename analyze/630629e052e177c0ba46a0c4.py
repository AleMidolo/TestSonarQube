def parse_diaspora_webfinger(document: str) -> Dict:
    """
    Parse Diaspora webfinger which is either in JSON format (new) or XRD (old).
    
    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    import json
    from xml.etree import ElementTree
    
    # Try parsing as JSON first (new format)
    try:
        data = json.loads(document)
        result = {
            'subject': data.get('subject', ''),
            'aliases': data.get('aliases', []),
            'links': []
        }
        
        # Parse links
        for link in data.get('links', []):
            if 'rel' in link and 'href' in link:
                result['links'].append({
                    'rel': link['rel'],
                    'href': link['href'],
                    'type': link.get('type', '')
                })
        return result
        
    except json.JSONDecodeError:
        # Try parsing as XRD (old format) 
        try:
            # Add XML namespace
            ns = {'xrd': 'http://docs.oasis-open.org/ns/xri/xrd-1.0'}
            
            root = ElementTree.fromstring(document)
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
                    'href': link.get('href', ''),
                    'type': link.get('type', '')
                }
                result['links'].append(link_data)
                
            return result
            
        except ElementTree.ParseError:
            raise ValueError("Document is neither valid JSON nor valid XML")