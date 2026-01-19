def format_line_html_text(self, html_text):
    """
    获取不包含代码的 HTML 文本,并在代码所在的位置添加 -CODE- 标签
    :param html_text:string
    :return:string
    """
    from bs4 import BeautifulSoup
    
    # 解析 HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # 找到所有的 <pre> 和 <code> 标签,替换为 -CODE-
    for tag in soup.find_all(['pre', 'code']):
        # 如果是 pre 标签内的 code,只替换 pre
        if tag.name == 'code' and tag.parent and tag.parent.name == 'pre':
            continue
        tag.replace_with('-CODE-')
    
    # 获取纯文本
    text = soup.get_text()
    
    # 清理多余的空行,保持格式整洁
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    return '\n'.join(lines)