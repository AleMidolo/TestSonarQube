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
    all_text = soup.get_text(separator='\n')
    code_elements = soup.find_all(['pre', 'code', 'blockquote'])
    formatted_lines = []
    lines = all_text.split('\n')
    line_index = 0
    for element in soup.find_all(True):
        if element.name in ['pre', 'code', 'blockquote']:
            element_text = element.get_text(strip=True)
            if element_text:
                formatted_lines.append(self.CODE_MARK)
                element_lines = element_text.split('\n')
                line_index += len([l for l in element_lines if l.strip()])
        elif element.string and element.string.strip():
            formatted_lines.append(element.string.strip())
    if not formatted_lines:
        text_without_code = soup.get_text(separator='\n')
        for element in code_elements:
            element_text = element.get_text()
            if element_text:
                text_without_code = text_without_code.replace(element_text, self.CODE_MARK)
        lines = text_without_code.split('\n')
        formatted_lines = []
        for line in lines:
            line = line.strip()
            if line:
                formatted_lines.append(line)
        result = []
        prev_was_code = False
        for line in formatted_lines:
            if line == self.CODE_MARK:
                if not prev_was_code:
                    result.append(line)
                prev_was_code = True
            else:
                result.append(line)
                prev_was_code = False
        formatted_lines = result
    result_text = '\n'.join(formatted_lines)
    return self.__format_line_feed(result_text)