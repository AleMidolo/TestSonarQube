from typing import Optional
import requests

def fetch_content_type(url: str) -> Optional[str]:
    """
    रिमोट यूआरएल का हेड प्राप्त करें ताकि कंटेंट टाइप निर्धारित किया जा सके।
    """
    try:
        response = requests.head(url)
        return response.headers.get('Content-Type')
    except requests.RequestException:
        return None