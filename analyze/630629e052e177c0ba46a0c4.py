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
            links = data.get('links', [])
            for link in links:
                if isinstance(link, dict) and link.get('rel') == 'http://microformats.org/profile/hcard':
                    return {'hcard_url': link.get('href')}
        return {}
    except json.JSONDecodeError:
        # Handle XRD format if necessary
        # For simplicity, this example only handles JSON format
        return {}