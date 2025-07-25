import requests
from typing import Optional

def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    try:
        # 解析handle，获取用户名和域名
        username, domain = handle.split('@')
        
        # 构建WebFinger请求URL
        url = f"https://{domain}/.well-known/webfinger?resource=acct:{username}@{domain}"
        
        # 发送GET请求
        response = requests.get(url, headers={"Accept": "application/jrd+json"})
        
        # 检查响应状态码
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None