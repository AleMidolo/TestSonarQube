import json
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    通过读取 JSON 格式的文档获取 Webfinger，Webfinger 中的 `hcard_url` 值是文档中 `links` 的 `href` 值。

    解析 Diaspora 的 Webfinger，该 Webfinger 可以是 JSON 格式（新格式）或 XRD 格式（旧格式）。

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    try:
        data = json.loads(document)
        if isinstance(data, dict):
            if 'links' in data:
                for link in data['links']:
                    if isinstance(link, dict) and 'rel' in link and link['rel'] == 'http://microformats.org/profile/hcard':
                        return {'hcard_url': link.get('href')}
            elif 'subject' in data:
                # Handle XRD format (old format)
                for link in data.get('links', []):
                    if isinstance(link, dict) and 'rel' in link and link['rel'] == 'http://microformats.org/profile/hcard':
                        return {'hcard_url': link.get('href')}
        return {}
    except json.JSONDecodeError:
        # Handle XRD format (old format)
        from xml.etree import ElementTree as ET
        try:
            root = ET.fromstring(document)
            for link in root.findall('{http://docs.oasis-open.org/ns/xri/xrd-1.0}Link'):
                if link.get('rel') == 'http://microformats.org/profile/hcard':
                    return {'hcard_url': link.get('href')}
            return {}
        except ET.ParseError:
            return {}