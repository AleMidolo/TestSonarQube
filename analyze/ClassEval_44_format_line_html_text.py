def format_line_html_text(self, html_text):
    """
    कोड के बिना एचटीएमएल टेक्स्ट प्राप्त करें, और जहां कोड है वहां -CODE- टैग जोड़ें
    :param html_text:string
    :return:string
    """
    from html.parser import HTMLParser
    
    class CodeHTMLParser(HTMLParser):
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
            
            # Check if we're exiting a code block
            if tag in self.code_tags:
                # Check if there are no more code tags in the stack
                if not any(t in self.code_tags for t in self.tag_stack):
                    self.in_code_block = False
                    self.result.append('-CODE-')
                    
        def handle_data(self, data):
            if not self.in_code_block:
                text = data.strip()
                if text:
                    self.result.append(text)
                    
        def get_result(self):
            return '\n'.join(self.result)
    
    parser = CodeHTMLParser()
    parser.feed(html_text)
    return parser.get_result()