import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    रिमोट यूआरएल का हेड प्राप्त करें ताकि कंटेंट टाइप निर्धारित किया जा सके।
    """
    try:
        response = requests.head(url, timeout=5)
        response.raise_for_status()
        return response.headers.get('Content-Type')
    except (requests.RequestException, ValueError):
        return None