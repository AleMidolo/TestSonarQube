def extract_code_from_html_text(self, html_text):
    """
        extraer códigos del cuerpo html
        :param html_text: cadena, texto html
        :return: la lista de códigos
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Título</h1>
        >>>    <p>Este es un párrafo.</p>
        >>>    <pre>print('¡Hola, mundo!')</pre>
        >>>    <p>Otro párrafo.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('¡Hola, mundo!')", 'for i in range(5):
                print(i)']
        """
    if html_text is None or len(html_text) == 0:
        return []
    soup = BeautifulSoup(html_text, 'lxml')
    code_elements = soup.find_all(name=['pre', 'code'])
    extracted_codes = []
    for element in code_elements:
        code_text = element.get_text()
        cleaned_code = code_text.strip()
        if cleaned_code:
            extracted_codes.append(cleaned_code)
    return extracted_codes