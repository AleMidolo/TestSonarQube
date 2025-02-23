from typing import Dict
import json
import xml.etree.ElementTree as ET

def parse_diaspora_webfinger(document: str) -> Dict:
    """
    通过读取 JSON 格式的文档获取 Webfinger，Webfinger 中的 `hcard_url` 值是文档中 `links` 的 `href` 值。

    解析 Diaspora 的 Webfinger，该 Webfinger 可以是 JSON 格式（新格式）或 XRD 格式（旧格式）。

    https://diaspora.github.io/diaspora_federation/discovery/webfinger.html
    """
    try:
        # Try to parse as JSON
        data = json.loads(document)
        if 'links' in data:
            for link in data['links']:
                if 'rel' in link and link['rel'] == 'http://webfinger.net/rel/hcard':
                    return {'hcard_url': link['href']}
    except json.JSONDecodeError:
        pass

    try:
        # Try to parse as XRD (XML)
        root = ET.fromstring(document)
        for link in root.findall('{http://docs.oasis-open.org/ns/xri/xrd-1.0}Link'):
            rel = link.get('rel')
            if rel == 'http://webfinger.net/rel/hcard':
                return {'hcard_url': link.get('href')}
    except ET.ParseError:
        pass

    return {}