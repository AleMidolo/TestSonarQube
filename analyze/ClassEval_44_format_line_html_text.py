def format_line_html_text(self, html_text):
    """
        कोड के बिना एचटीएमएल टेक्स्ट प्राप्त करें, और जहां कोड है वहां -CODE- टैग जोड़ें
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>शीर्षक</h1>
        >>>    <p>यह एक पैराग्राफ है।</p>
        >>>    <pre>print('नमस्ते, दुनिया!')</pre>
        >>>    <p>एक और पैराग्राफ।</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        शीर्षक
        यह एक पैराग्राफ है।
        -CODE-
        एक और पैराग्राफ।
        -CODE-
        """
    soup = BeautifulSoup(html_text, 'lxml')
    for script in soup(['script', 'style']):
        script.decompose()
    result_lines = []
    for element in soup.find_all(recursive=True):
        if element.name in ['pre', 'blockquote']:
            result_lines.append(self.CODE_MARK)
        elif element.string:
            text = element.string.strip()
            if text:
                result_lines.append(text)
        elif element.get_text(strip=True):
            text = element.get_text(strip=True)
            if text:
                result_lines.append(text)
    result = '\n'.join(result_lines)
    return self.__format_line_feed(result)