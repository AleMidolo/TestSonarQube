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
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
        if html_text is None or len(html_text) == 0:
            return []
        soup = BeautifulSoup(html_text, 'lxml')
        code_snippets = []
        code_tags = soup.find_all(name=['pre', 'code'])
        for tag in code_tags:
            code_snippets.append(tag.get_text())
        return code_snippets