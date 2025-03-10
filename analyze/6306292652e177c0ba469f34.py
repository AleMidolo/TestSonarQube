import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    """
    通过 URL 和 USER_AGENT 设置请求的头部。

    通过获取远程 URL 的 HEAD 请求来确定内容类型。
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.head(url, headers=headers, timeout=5)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        return content_type
    except requests.RequestException:
        return None