def format_line_html_text(self, html_text):
    """
        获取不包含代码的 HTML 文本，并在代码所在的位置添加 -CODE- 标签
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>标题</h1>
        >>>    <p>这是一个段落。</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>另一个段落。</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        标题
        这是一个段落。
        -CODE-
        另一个段落。
        -CODE-
        """
    soup = BeautifulSoup(html_text, 'lxml')
    for script in soup(['script', 'style']):
        script.decompose()
    all_elements = soup.find_all(True)
    result_parts = []
    for element in all_elements:
        if element.find_parents(['script', 'style']):
            continue
        if element.name in ['pre', 'blockquote']:
            result_parts.append(self.CODE_MARK)
        elif element.name in ['code']:
            if not element.find_parents(['pre', 'blockquote']):
                result_parts.append(self.CODE_MARK)
        else:
            text = element.get_text(strip=False)
            if text and element.parent.name not in ['pre', 'blockquote', 'code']:
                result_parts.append(text)
    result = '\n'.join(result_parts)
    result = re.sub('\\n\\s*\\n+', '\n', result)
    result = result.strip()
    return result