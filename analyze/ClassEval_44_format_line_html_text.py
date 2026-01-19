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
        if isinstance(element, str):
            if element.strip():
                parent = element.parent
                if parent and parent.name in ['pre', 'blockquote']:
                    if result_lines and result_lines[-1] != self.CODE_MARK:
                        result_lines.append(self.CODE_MARK)
                else:
                    text = element.strip()
                    if text:
                        result_lines.append(text)
        elif element.name in ['br', 'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
            if result_lines and result_lines[-1] != '':
                result_lines.append('')
    result = '\n'.join(result_lines)
    result = re.sub('\\n\\s*\\n', '\n', result)
    result = result.strip()
    return result