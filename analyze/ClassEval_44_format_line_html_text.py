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
    for code_element in soup.find_all(['pre', 'blockquote']):
        code_element.replace_with(self.CODE_MARK)
    text = soup.get_text(separator='\n', strip=False)
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            cleaned_lines.append(stripped_line)
        elif self.CODE_MARK in line:
            cleaned_lines.append(self.CODE_MARK)
    result = '\n'.join(cleaned_lines)
    return self.__format_line_feed(result)