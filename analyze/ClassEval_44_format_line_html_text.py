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
    code_elements = soup.find_all(['pre', 'code', 'blockquote'])
    for element in code_elements:
        element.replace_with(self.CODE_MARK)
    text = soup.get_text(separator='\n', strip=False)
    text = re.sub('\\n\\s*\\n', '\n', text)
    text = re.sub('[ \\t]+', ' ', text)
    text = self.__format_line_feed(text)
    return text.strip()