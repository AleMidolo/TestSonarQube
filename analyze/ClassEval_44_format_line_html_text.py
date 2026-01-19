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
    code_tags = soup.find_all(['pre', 'blockquote'])
    for tag in code_tags:
        tag.replace_with(self.CODE_MARK)
    text = soup.get_text()
    text = re.sub('\\s+', ' ', text)
    text = re.sub('\\n\\s*\\n', '\n', text)
    text = text.strip()
    return text