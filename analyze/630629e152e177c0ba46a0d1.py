def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
    """
    尝试检索一个符合RFC7033标准的WebFinger文档。如果失败，不会抛出异常。
    """
    import requests
    from urllib.parse import urlparse, quote
    from typing import Optional

    try:
        # 解析handle格式 user@domain.com
        if '@' not in handle:
            return None
            
        username, domain = handle.split('@')
        
        # 构建WebFinger URL
        webfinger_url = f"https://{domain}/.well-known/webfinger"
        params = {
            'resource': f'acct:{quote(username)}@{domain}'
        }
        
        # 发送请求
        response = requests.get(
            webfinger_url,
            params=params,
            headers={'Accept': 'application/jrd+json'},
            timeout=10
        )
        
        # 检查响应状态
        if response.status_code == 200:
            return response.text
            
    except (requests.RequestException, ValueError):
        pass
        
    return None