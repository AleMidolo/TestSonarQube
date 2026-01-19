def format_line_html_text(self, html_text):
    """
    get the html text without the code, and add the code tag -CODE- where the code is
    :param html_text:string
    :return:string
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.format_line_html_text(<html>
    >>> <body>
    >>>    <h1>Title</h1>
    >>>    <p>This is a paragraph.</p>
    >>>    <pre>print('Hello, world!')</pre>
    >>>    <p>Another paragraph.</p>
    >>>    <pre><code>for i in range(5):
    >>>    print(i)</code></pre>
    >>>    </body>
    >>>    </html>)
    Title
    This is a paragraph.
    -CODE-
    Another paragraph.
    -CODE-
    """
    from bs4 import BeautifulSoup
    
    # Parse the HTML
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all <pre> tags (which typically contain code)
    for pre_tag in soup.find_all('pre'):
        # Replace the <pre> tag with -CODE- text
        pre_tag.replace_with('-CODE-')
    
    # Get the text content, which will strip HTML tags
    text = soup.get_text()
    
    # Clean up extra whitespace while preserving line structure
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    return '\n'.join(lines)