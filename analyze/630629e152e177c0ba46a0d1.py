import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    try:
        # 假设handle是类似"user@example.com"的格式
        parts = handle.split('@')
        if len(parts) != 2:
            return None
        
        domain = parts[1]
        webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
        
        response = requests.get(webfinger_url, timeout=5)
        response.raise_for_status()
        
        return response.text
    except (requests.RequestException, ValueError):
        return None