def extract_code_from_html_text(self, html_text):
    """
        एचटीएमएल बॉडी से कोड निकालें
        :param html_text: स्ट्रिंग, एचटीएमएल टेक्स्ट
        :return: कोड की सूची
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>शीर्षक</h1>
        >>>    <p>यह एक पैराग्राफ है।</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>एक और पैराग्राफ।</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):
                print(i)']
        """
    if html_text is None or len(html_text) == 0:
        return []
    soup = BeautifulSoup(html_text, 'lxml')
    code_elements = soup.find_all(['pre', 'code'])
    extracted_code = []
    for element in code_elements:
        code_text = element.get_text().strip()
        if code_text:
            code_text = re.sub('\\r\\n', '\n', code_text)
            code_text = re.sub('\\n\\s*\\n', '\n', code_text)
            extracted_code.append(code_text)
    return extracted_code