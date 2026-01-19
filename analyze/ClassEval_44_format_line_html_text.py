def format_line_html_text(self, html_text):
    """
    get the html text without the code, and add the code tag -CODE- where the code is
    :param html_text:string
    :return:string
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.format_line_html_text(<html>
    >>> <body>
    >>>    <h1>Title</h1>
    >>>    <p>This is a paragraph.</p>
    >>>    <pre>print('Hello, world!')</pre>
    >>>    <p>Another paragraph.</p>
    >>>    <pre><code>for i in range(5):
    >>>    print(i)</code></pre>
    >>>    </body>
    >>>    </html>)
    Title
    This is a paragraph.
    -CODE-
    Another paragraph.
    -CODE-
    """
    from html.parser import HTMLParser
    
    class CodeReplacer(HTMLParser):
        def __init__(self):
            super().__init__()
            self.result = []
            self.in_pre = False
            self.in_code = False
            
        def handle_starttag(self, tag, attrs):
            if tag == 'pre':
                self.in_pre = True
            elif tag == 'code':
                self.in_code = True
                
        def handle_endtag(self, tag):
            if tag == 'pre':
                if self.in_pre:
                    self.result.append('-CODE-')
                self.in_pre = False
            elif tag == 'code':
                self.in_code = False
                
        def handle_data(self, data):
            if not self.in_pre and not self.in_code:
                text = data.strip()
                if text:
                    self.result.append(text)
                    
        def get_result(self):
            return '\n'.join(self.result)
    
    parser = CodeReplacer()
    parser.feed(html_text)
    return parser.get_result()