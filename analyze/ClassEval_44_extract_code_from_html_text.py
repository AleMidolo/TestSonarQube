def extract_code_from_html_text(self, html_text):
    """
        estrae i codici dal corpo html
        :param html_text: stringa, testo html
        :return: la lista di codici
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Titolo</h1>
        >>>    <p>Questo è un paragrafo.</p>
        >>>    <pre>print('Ciao, mondo!')</pre>
        >>>    <p>Un altro paragrafo.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Ciao, mondo!')", 'for i in range(5):
                print(i)']
        """
    if html_text is None or len(html_text) == 0:
        return []
    soup = BeautifulSoup(html_text, 'lxml')
    code_elements = soup.find_all(name=['pre', 'code'])
    extracted_codes = []
    for element in code_elements:
        code_text = element.get_text(strip=False)
        if code_text:
            cleaned_code = code_text.strip()
            if cleaned_code:
                extracted_codes.append(cleaned_code)
    return extracted_codes