def extract_code_from_html_text(self, html_text):
    """
    extract codes from the html body
    :param html_text: string, html text
    :return: the list of code
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.extract_code_from_html_text(<html>
    >>> <body>
    >>>    <h1>Title</h1>
    >>>    <p>This is a paragraph.</p>
    >>>    <pre>print('Hello, world!')</pre>
    >>>    <p>Another paragraph.</p>
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
            self.codes = []
            self.in_pre = False
            self.current_code = []
        
        def handle_starttag(self, tag, attrs):
            if tag == 'pre':
                self.in_pre = True
                self.current_code = []
        
        def handle_endtag(self, tag):
            if tag == 'pre':
                self.in_pre = False
                if self.current_code:
                    self.codes.append(''.join(self.current_code))
                    self.current_code = []
        
        def handle_data(self, data):
            if self.in_pre:
                self.current_code.append(data)
    
    parser = CodeExtractor()
    parser.feed(html_text)
    return parser.codes