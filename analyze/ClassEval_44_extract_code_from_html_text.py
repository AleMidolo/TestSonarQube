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
    code_elements = []
    pre_tags = soup.find_all('pre')
    code_tags = soup.find_all('code')
    for pre in pre_tags:
        code_in_pre = pre.find('code')
        if code_in_pre:
            code_text = code_in_pre.get_text(strip=False)
        else:
            code_text = pre.get_text(strip=False)
        if code_text:
            code_elements.append(code_text)
    for code in code_tags:
        if not code.find_parent('pre'):
            code_text = code.get_text(strip=False)
            if code_text:
                code_elements.append(code_text)
    seen = set()
    unique_code_elements = []
    for code in code_elements:
        if code not in seen:
            seen.add(code)
            unique_code_elements.append(code)
    return unique_code_elements