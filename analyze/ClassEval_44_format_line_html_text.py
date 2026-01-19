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
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all <pre> and <code> tags and replace them with -CODE- placeholder
    for tag in soup.find_all(['pre', 'code']):
        tag.replace_with('-CODE-')
    
    # Get the text content
    text = soup.get_text()
    
    # Clean up the text: remove extra whitespace and normalize line breaks
    lines = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    
    return '\n'.join(lines)