def format_line_html_text(self, html_text):
    """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text('<html><body><h1>Title</h1><p>This is a paragraph.</p><pre>print('Hello, world!')</pre><p>Another paragraph.</p><pre><code>for i in range(5):
    print(i)</code></pre></body></html>')
        'Title
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
'
        """
    soup = BeautifulSoup(html_text, 'lxml')
    for code in soup.find_all(['pre', 'code']):
        code.insert_before(self.CODE_MARK)
        code.insert_after(self.CODE_MARK)
        code.unwrap()
    return self.__format_line_feed(soup.get_text())