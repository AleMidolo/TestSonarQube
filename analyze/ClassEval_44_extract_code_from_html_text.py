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
    from html.parser import HTMLParser
    
    class CodeExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.code_blocks = []
            self.current_code = []
            self.in_pre = False
            self.in_code = False
            
        def handle_starttag(self, tag, attrs):
            if tag == 'pre':
                self.in_pre = True
                self.current_code = []
            elif tag == 'code' and self.in_pre:
                self.in_code = True
                
        def handle_endtag(self, tag):
            if tag == 'pre':
                if self.current_code:
                    code_text = ''.join(self.current_code)
                    self.code_blocks.append(code_text)
                self.in_pre = False
                self.in_code = False
                self.current_code = []
            elif tag == 'code':
                self.in_code = False
                
        def handle_data(self, data):
            if self.in_pre:
                self.current_code.append(data)
    
    parser = CodeExtractor()
    parser.feed(html_text)
    return parser.code_blocks