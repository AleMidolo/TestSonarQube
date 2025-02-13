import json
from typing import Dict, Any

def parse_diaspora_webfinger(document: str) -> Dict:
    try:
        # Try to parse the document as JSON
        data = json.loads(document)
        if 'links' in data:
            for link in data['links']:
                if 'rel' in link and link['rel'] == 'http://webfinger.net/rel/profile':
                    return {'hcard_url': link['href']}
    except json.JSONDecodeError:
        pass

    # If JSON parsing fails, try to parse as XRD (old format)
    # This is a simple implementation and may need to be adjusted for full XRD support
    lines = document.splitlines()
    for line in lines:
        if '<Link' in line and 'rel="http://webfinger.net/rel/profile"' in line:
            start = line.find('href="') + len('href="')
            end = line.find('"', start)
            hcard_url = line[start:end]
            return {'hcard_url': hcard_url}

    return {}