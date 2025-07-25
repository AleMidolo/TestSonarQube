def fetch_content_type(url: str) -> Optional[str]:
    """
    通过 URL 和 USER_AGENT 设置请求的头部。

    通过获取远程 URL 的 HEAD 请求来确定内容类型。
    """
    import requests
    from typing import Optional

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发送 HEAD 请求
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=10)
        
        # 获取 Content-Type
        content_type = response.headers.get('Content-Type')
        
        # 如果存在分号,只返回分号前的内容类型
        if content_type and ';' in content_type:
            content_type = content_type.split(';')[0]
            
        return content_type

    except requests.RequestException:
        return None