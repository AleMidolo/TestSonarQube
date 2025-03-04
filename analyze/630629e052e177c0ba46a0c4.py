def parse_diaspora_webfinger(document: str) -> Dict:
    """
    通过读取 JSON 格式的文档获取 Webfinger，Webfinger 中的 `hcard_url` 值是文档中 `links` 的 `href` 值。

    解析 Diaspora 的 Webfinger，该 Webfinger 可以是 JSON 格式（新格式）或 XRD 格式（旧格式）。

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    import json
    from typing import Dict
    import xml.etree.ElementTree as ET

    # Try parsing as JSON first
    try:
        data = json.loads(document)
        
        # Look for hcard_url in links
        for link in data.get('links', []):
            if link.get('rel') == 'http://microformats.org/profile/hcard':
                return {'hcard_url': link.get('href')}
                
    except json.JSONDecodeError:
        # If JSON parsing fails, try XRD format
        try:
            # Remove XML namespace to simplify parsing
            document = document.replace('xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0"', '')
            root = ET.fromstring(document)
            
            # Find Link element with hcard rel
            for link in root.findall('.//Link'):
                if link.get('rel') == 'http://microformats.org/profile/hcard':
                    return {'hcard_url': link.get('href')}
                    
        except ET.ParseError:
            pass
            
    # Return empty dict if no hcard_url found
    return {'hcard_url': None}