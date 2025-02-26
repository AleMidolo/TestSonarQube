from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    try:
        url = f"https://webfinger.example.com/whois/{handle}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None