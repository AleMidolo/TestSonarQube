def format_line_html_text(self, html_text):
    """
        ottiene il testo html senza il codice e aggiunge il tag di codice -CODE- dove si trova il codice
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Titolo</h1>
        >>>    <p>Questo è un paragrafo.</p>
        >>>    <pre>print('Ciao, mondo!')</pre>
        >>>    <p>Un altro paragrafo.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Titolo
        Questo è un paragrafo.
        -CODE-
        Un altro paragrafo.
        -CODE-
        """
    soup = BeautifulSoup(html_text, 'lxml')
    for script in soup(['script', 'style']):
        script.decompose()
    result_lines = []
    for element in soup.body.descendants if soup.body else soup.descendants:
        if isinstance(element, str) and element.parent.name not in ['pre', 'code', 'blockquote']:
            stripped = element.strip()
            if stripped:
                result_lines.append(stripped)
        elif element.name in ['pre', 'code', 'blockquote']:
            parent = element.parent
            if parent.name not in ['pre', 'code', 'blockquote']:
                result_lines.append(self.CODE_MARK)
    result = '\n'.join(result_lines)
    return self.__format_line_feed(result)