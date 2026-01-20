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
    from bs4 import BeautifulSoup
    
    # Parse the HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all <pre> and <code> tags and replace them with -CODE-
    for tag in soup.find_all(['pre', 'code']):
        # Replace the tag with a placeholder
        tag.replace_with('-CODE-')
    
    # Get the text content
    text = soup.get_text()
    
    # Clean up the text: remove extra whitespace and blank lines
    lines = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    
    # Join lines and return
    result = '\n'.join(lines)
    
    return result