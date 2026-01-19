def format_line_html_text(self, html_text):
    """
        ottiene il testo html senza il codice e aggiunge il tag di codice -CODE- dove si trova il codice
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text('<html><body><h1>Titolo</h1><p>Questo è un paragrafo.</p><pre>print('Ciao, mondo!')</pre><p>Un altro paragrafo.</p><pre><code>for i in range(5):
    print(i)</code></pre></body></html>')
        'Titolo
Questo è un paragrafo.
-CODE-
Un altro paragrafo.
-CODE-
'
        """
    soup = BeautifulSoup(html_text, 'lxml')
    text_parts = []
    for element in soup.find_all(['h1', 'p']):
        text_parts.append(element.get_text())
    code_tags = soup.find_all(['pre', 'code'])
    for _ in code_tags:
        text_parts.append(self.CODE_MARK)
    return '\n'.join(text_parts)