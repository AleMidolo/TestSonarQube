def process_text_links(text):
    """
    处理文本中的链接，添加一些属性并将文本链接转换为可点击的超链接。
    """
    import re

    # 正则表达式匹配链接
    url_pattern = r'(https?://[^\s]+)'
    
    # 替换链接为可点击的超链接
    def replace_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # 使用sub方法替换文本中的链接
    processed_text = re.sub(url_pattern, replace_link, text)
    
    return processed_text