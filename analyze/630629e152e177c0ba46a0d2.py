import requests
from urllib.parse import urlparse
from lxml import etree

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    检索并解析远程 Diaspora WebFinger 文档。

    :arg handle: 要检索的远程句柄
    :returns: 字典
    """
    # 解析句柄，获取用户名和域名
    username, domain = handle.split('@')
    
    # 构造 WebFinger URL
    webfinger_url = f"https://{domain}/.well-known/webfinger?resource=acct:{handle}"
    
    try:
        # 发送 GET 请求获取 WebFinger 文档
        response = requests.get(webfinger_url)
        response.raise_for_status()
        
        # 解析 XML 文档
        root = etree.fromstring(response.content)
        
        # 提取所需信息
        result = {}
        for link in root.findall("{http://webfinger.net/rel/profile-page}"):
            result['profile_page'] = link.get('href')
        
        for link in root.findall("{http://webfinger.net/rel/avatar}"):
            result['avatar'] = link.get('href')
        
        for link in root.findall("{http://webfinger.net/rel/hcard}"):
            result['hcard'] = link.get('href')
        
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving WebFinger document: {e}")
        return {}
    except etree.XMLSyntaxError as e:
        print(f"Error parsing WebFinger document: {e}")
        return {}