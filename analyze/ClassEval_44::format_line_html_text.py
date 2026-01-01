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
    for tag in soup.find_all(['pre', 'blockquote']):
        tag.replace_with(self.CODE_MARK)
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    text = '\n'.join(lines)
    text = re.sub(f'{re.escape(self.CODE_MARK)}(\\s*{re.escape(self.CODE_MARK)})+', self.CODE_MARK, text)
    return text