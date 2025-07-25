import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    रिमोट यूआरएल का हेड प्राप्त करें ताकि कंटेंट टाइप निर्धारित किया जा सके।
    """
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        return content_type
    except requests.RequestException:
        return None