import re
import string
import gensim
from bs4 import BeautifulSoup

class HtmlUtil: 
    def __init__(self):
        """
        Initialize a series of labels
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    def __format_line_feed(self, text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        return re.sub(re.compile(r'\n+'), '\n', text)
    
    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text('<html><body><h1>Title</h1><p>This is a paragraph.</p><pre>print(\'Hello, world!\')</pre><p>Another paragraph.</p><pre><code>for i in range(5):\n    print(i)</code></pre></body></html>')
        ["print('Hello, world!')", 'for i in range(5):\n    print(i)']
        """
        text_with_code_tag = self.format_line_html_text(html_text)
    
        if self.CODE_MARK not in text_with_code_tag:
            return []
    
        code_index_start = 0
        soup = BeautifulSoup(html_text, 'lxml')
        code_tag = soup.find_all(name=['pre', 'blockquote'])
        code_count = text_with_code_tag.count(self.CODE_MARK)
        code_list = []
        for code_index in range(code_index_start, code_index_start + code_count):
            code = code_tag[code_index].get_text()
            if code:
                code_list.append(code)
        return code_list
    
    def format_line_html_text(self, html_text):
        """
        ottiene il testo html senza il codice e aggiunge il tag di codice -CODE- dove si trova il codice
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text('<html><body><h1>Titolo</h1><p>Questo è un paragrafo.</p><pre>print(\'Ciao, mondo!\')</pre><p>Un altro paragrafo.</p><pre><code>for i in range(5):\n    print(i)</code></pre></body></html>')
        'Titolo\nQuesto è un paragrafo.\n-CODE-\nUn altro paragrafo.\n-CODE-\n'
        """
        soup = BeautifulSoup(html_text, 'lxml')
        text_parts = []
        for element in soup.body.find_all(True):  # Find all tags
            if element.name in ['pre', 'code']:
                text_parts.append(self.CODE_MARK)
            else:
                text_parts.append(element.get_text())
        return self.__format_line_feed('\n'.join(text_parts))