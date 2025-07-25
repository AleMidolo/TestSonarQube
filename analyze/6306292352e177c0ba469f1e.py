def process_text_links(text):
    """
    处理文本中的链接，添加一些属性并将文本链接转换为可点击的超链接。
    """
    import re
    
    # 匹配URL的正则表达式模式
    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
    
    def replace_url(match):
        url = match.group(0)
        # 如果URL不以http开头,添加http://
        if url.startswith('www.'):
            url = 'http://' + url
            
        # 构建带属性的HTML链接标签
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # 使用正则表达式替换所有匹配的URL
    processed_text = re.sub(url_pattern, replace_url, text)
    
    return processed_text