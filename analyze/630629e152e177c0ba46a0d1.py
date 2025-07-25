import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    try:
        # 假设WebFinger文档的URL格式为 https://example.com/.well-known/webfinger?resource=acct:handle
        url = f"https://{handle.split('@')[1]}/.well-known/webfinger"
        params = {'resource': f'acct:{handle}'}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except (requests.RequestException, IndexError):
        return None