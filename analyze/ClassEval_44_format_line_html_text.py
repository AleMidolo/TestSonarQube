def format_line_html_text(self, html_text):
    """
    कोड के बिना एचटीएमएल टेक्स्ट प्राप्त करें, और जहां कोड है वहां -CODE- टैग जोड़ें
    :param html_text:string
    :return:string
    """
    from html.parser import HTMLParser
    
    class CodeReplacerParser(HTMLParser):
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
                
                # Add -CODE- marker when exiting code block
                if not self.in_code_block:
                    self.result.append('-CODE-')
        
        def handle_data(self, data):
            if not self.in_code_block:
                # Only add non-empty text
                text = data.strip()
                if text:
                    self.result.append(text)
    
    parser = CodeReplacerParser()
    parser.feed(html_text)
    
    # Join with newlines and return
    return '\n'.join(parser.result)