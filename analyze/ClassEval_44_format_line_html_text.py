def format_line_html_text(self, html_text):
    """
    获取不包含代码的 HTML 文本，并在代码所在的位置添加 -CODE- 标签
    :param html_text:string
    :return:string
    """
    from bs4 import BeautifulSoup
    
    # Parse the HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all <pre> and <code> tags and replace them with -CODE- placeholder
    for tag in soup.find_all(['pre', 'code']):
        # Replace the tag with a special marker
        tag.replace_with('-CODE-')
    
    # Get the text content
    text = soup.get_text()
    
    # Clean up the text: remove extra whitespace and normalize line breaks
    lines = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    
    # Join lines and handle multiple consecutive -CODE- markers
    result = '\n'.join(lines)
    
    # Remove duplicate -CODE- markers that might appear consecutively
    while '-CODE-\n-CODE-' in result:
        result = result.replace('-CODE-\n-CODE-', '-CODE-')
    
    return result