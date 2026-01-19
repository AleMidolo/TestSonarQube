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
    elements = soup.find_all(text=True)
    result_parts = []
    for element in elements:
        parent = element.parent
        if parent.name in ['pre', 'code', 'blockquote']:
            if parent.name in ['pre', 'blockquote'] or (parent.name == 'code' and parent.parent.name in ['pre', 'blockquote']):
                if not result_parts or result_parts[-1] != self.CODE_MARK:
                    result_parts.append(self.CODE_MARK)
        else:
            text = element.strip()
            if text:
                result_parts.append(text)
    result = '\n'.join(result_parts)
    result = re.sub('\\n+', '\n', result)
    result = re.sub('(\\n' + re.escape(self.CODE_MARK) + ')+', '\n' + self.CODE_MARK, result)
    return result.strip()