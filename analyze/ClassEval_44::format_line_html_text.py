def format_line_html_text(self, html_text):
    """
        获取不包含代码的 HTML 文本，并在代码所在的位置添加 -CODE- 标签
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text('<html><body><h1>标题</h1><p>这是一个段落。</p><pre>print('Hello, world!')</pre><p>另一个段落。</p><pre><code>for i in range(5):
    print(i)</code></pre></body></html>')
        '标题
这是一个段落。
-CODE-
另一个段落。
-CODE-
'
        """
    soup = BeautifulSoup(html_text, 'lxml')
    for code in soup.find_all(['pre', 'code']):
        code.insert_before('\n' + self.CODE_MARK + '\n')
        code.insert_after('\n' + self.CODE_MARK + '\n')
    return self.__format_line_feed(soup.get_text())