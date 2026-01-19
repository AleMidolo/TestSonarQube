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
    code_elements = soup.find_all(['pre', 'blockquote'])
    for element in code_elements:
        element.replace_with(self.CODE_MARK)
    text = soup.get_text()
    text = re.sub('\\s+', ' ', text).strip()
    text = re.sub('(-CODE-\\s*)+', self.CODE_MARK + '\n', text)
    text = self.__format_line_feed(text)
    return text