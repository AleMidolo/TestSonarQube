def extract_code_from_html_text(self, html_text):
    """
    estrae i codici dal corpo html
    :param html_text: stringa, testo html
    :return: la lista di codici
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.extract_code_from_html_text(<html>
    >>> <body>
    >>>    <h1>Titolo</h1>
    >>>    <p>Questo è un paragrafo.</p>
    >>>    <pre>print('Ciao, mondo!')</pre>
    >>>    <p>Un altro paragrafo.</p>
    >>>    <pre><code>for i in range(5):
    >>>    print(i)</code></pre>
    >>>    </body>
    >>>    </html>)
    ["print('Ciao, mondo!')", 'for i in range(5):\n                print(i)']
    """
    from html.parser import HTMLParser
    
    class CodeExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.codes = []
            self.in_pre = False
            self.in_code = False
            self.current_code = []
        
        def handle_starttag(self, tag, attrs):
            if tag == 'pre':
                self.in_pre = True
                self.current_code = []
            elif tag == 'code' and self.in_pre:
                self.in_code = True
        
        def handle_endtag(self, tag):
            if tag == 'pre':
                if self.current_code:
                    code_text = ''.join(self.current_code).strip()
                    if code_text:
                        self.codes.append(code_text)
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
    return parser.codes