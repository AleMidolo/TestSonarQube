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
    elements = soup.find_all(text=True)
    result_parts = []
    for element in elements:
        parent = element.parent
        if parent.name in ['pre', 'code', 'blockquote']:
            if parent.name in ['pre', 'blockquote'] or (parent.name == 'code' and parent.parent.name in ['pre', 'blockquote']):
                if not result_parts or result_parts[-1] != self.CODE_MARK:
                    result_parts.append(self.CODE_MARK)
        else:
            text = element.strip()
            if text:
                result_parts.append(text)
    result = '\n'.join(result_parts)
    result = re.sub(f'({re.escape(self.CODE_MARK)}\n*)+', f'{self.CODE_MARK}\n', result)
    return result.strip()