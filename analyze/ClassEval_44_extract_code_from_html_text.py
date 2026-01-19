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
    ["print('¡Hola, mundo!')", 'for i in range(5):\n                print(i)']
    """
    import re
    from html import unescape
    
    # Find all <pre> tags and their content
    pre_pattern = r'<pre[^>]*>(.*?)</pre>'
    pre_matches = re.findall(pre_pattern, html_text, re.DOTALL | re.IGNORECASE)
    
    codes = []
    for match in pre_matches:
        # Remove <code> tags if present
        code_pattern = r'<code[^>]*>(.*?)</code>'
        code_match = re.search(code_pattern, match, re.DOTALL | re.IGNORECASE)
        
        if code_match:
            code_text = code_match.group(1)
        else:
            code_text = match
        
        # Unescape HTML entities and strip leading/trailing whitespace
        code_text = unescape(code_text).strip()
        
        if code_text:
            codes.append(code_text)
    
    return codes