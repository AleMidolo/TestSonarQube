def format_line_html_text(self, html_text):
    """
    obtener el texto html sin el código, y agregar la etiqueta de código -CODE- donde está el código
    :param html_text:string
    :return:string
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.format_line_html_text(<html>
    >>> <body>
    >>>    <h1>Título</h1>
    >>>    <p>Este es un párrafo.</p>
    >>>    <pre>print('¡Hola, mundo!')</pre>
    >>>    <p>Otro párrafo.</p>
    >>>    <pre><code>for i in range(5):
    >>>    print(i)</code></pre>
    >>>    </body>
    >>>    </html>)
    Título
    Este es un párrafo.
    -CODE-
    Otro párrafo.
    -CODE-
    """
    from html.parser import HTMLParser
    
    class CodeReplacer(HTMLParser):
        def __init__(self):
            super().__init__()
            self.result = []
            self.in_code_block = False
            self.code_tags = {'pre', 'code'}
            self.tag_stack = []
        
        def handle_starttag(self, tag, attrs):
            self.tag_stack.append(tag)
            if tag in self.code_tags:
                self.in_code_block = True
        
        def handle_endtag(self, tag):
            if self.tag_stack and self.tag_stack[-1] == tag:
                self.tag_stack.pop()
            
            if tag in self.code_tags:
                # Check if we're still in a code block
                self.in_code_block = any(t in self.code_tags for t in self.tag_stack)
                if not self.in_code_block:
                    self.result.append('-CODE-')
        
        def handle_data(self, data):
            if not self.in_code_block:
                stripped = data.strip()
                if stripped:
                    self.result.append(stripped)
    
    parser = CodeReplacer()
    parser.feed(html_text)
    
    return '\n'.join(parser.result)