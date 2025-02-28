import re

def process_text_links(text):
    """
    处理文本中的链接，添加一些属性并将文本链接转换为可点击的超链接。
    """
    # 正则表达式匹配URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    def replace_with_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # 使用正则表达式替换文本中的URL为超链接
    processed_text = url_pattern.sub(replace_with_link, text)
    
    return processed_text