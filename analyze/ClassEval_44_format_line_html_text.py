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
    for tag in soup.find_all(['pre', 'blockquote']):
        tag.replace_with(self.CODE_MARK)
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split('  '))
    text = '\n'.join((chunk for chunk in chunks if chunk))
    text = self.__format_line_feed(text)
    return text