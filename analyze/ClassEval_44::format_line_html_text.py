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
    for element in soup.body.find_all(True):
        if element.name in ['pre', 'code']:
            text_parts.append(self.CODE_MARK)
        else:
            text_parts.append(element.get_text())
    return self.__format_line_feed('\n'.join(text_parts))