def extract_code_from_html_text(self, html_text):
        """
        从 HTML 正文中提取代码
        :param html_text: 字符串，HTML 文本
        :return: 代码列表
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>标题</h1>
        >>>    <p>这是一个段落。</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>另一个段落。</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
        if html_text is None or len(html_text) == 0:
            return []
        soup = BeautifulSoup(html_text, 'lxml')
        code_snippets = []
        code_tags = soup.find_all(name=['pre', 'code'])
        for tag in code_tags:
            code_snippets.append(tag.get_text())
        return code_snippets