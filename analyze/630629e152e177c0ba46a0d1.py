from typing import Optional
import requests

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    try:
        # Construct the WebFinger URL
        webfinger_url = f"https://{handle}/.well-known/webfinger?resource=acct:{handle}"
        response = requests.get(webfinger_url)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None