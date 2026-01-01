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
    soup = BeautifulSoup(html_text, 'lxml')
    for script in soup(['script', 'style']):
        script.decompose()
    for tag in soup.find_all(['pre', 'blockquote']):
        tag.replace_with(self.CODE_MARK)
    text = soup.get_text()
    text = self.__format_line_feed(text)
    text = re.sub('\\s*' + re.escape(self.CODE_MARK) + '\\s*', '\n' + self.CODE_MARK + '\n', text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)