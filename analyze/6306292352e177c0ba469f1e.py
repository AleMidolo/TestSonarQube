def process_text_links(text):
    """
    处理文本中的链接，添加一些属性并将文本链接转换为可点击的超链接。
    """
    import re
    
    # 匹配URL的正则表达式模式
    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
    
    def replace_url(match):
        url = match.group(0)
        # 如果URL不是以http开头,添加http://
        if url.startswith('www.'):
            url = 'http://' + url
            
        # 构建HTML链接,添加target="_blank"在新窗口打开
        # 添加rel="noopener noreferrer"增加安全性
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # 使用re.sub替换所有匹配的URL为HTML链接
    processed_text = re.sub(url_pattern, replace_url, text)
    
    return processed_text