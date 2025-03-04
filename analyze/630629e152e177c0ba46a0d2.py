def retrieve_and_parse_diaspora_webfinger(handle):
    """
    检索并解析远程 Diaspora WebFinger 文档。

    :arg handle: 要检索的远程句柄 
    :returns: 字典
    """
    import requests
    import json
    from urllib.parse import urlparse

    # 验证句柄格式
    if '@' not in handle:
        raise ValueError("Invalid handle format")

    username, domain = handle.split('@')
    
    # 构建 WebFinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # 发送请求获取 WebFinger 文档
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # 解析 JSON 响应
        data = response.json()
        
        # 提取相关信息到字典
        result = {
            'username': username,
            'domain': domain,
            'subject': data.get('subject', ''),
            'aliases': data.get('aliases', []),
            'links': {}
        }
        
        # 解析链接
        for link in data.get('links', []):
            rel = link.get('rel', '')
            if rel:
                result['links'][rel] = {
                    'href': link.get('href', ''),
                    'type': link.get('type', '')
                }
                
        return result
        
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to retrieve WebFinger document: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Invalid WebFinger document format")