def extract_code_from_html_text(self, html_text):
    """
    从 HTML 正文中提取代码
    :param html_text: 字符串，HTML 文本
    :return: 代码列表
    >>>htmlutil = HtmlUtil()
    >>>htmlutil.extract_code_from_html_text(<html>
    >>> <body>
    >>>    <h1>标题</h1>
    >>>    <p>这是一个段落。</p>
    >>>    <pre>print('Hello, world!')</pre>
    >>>    <p>另一个段落。</p>
    >>>    <pre><code>for i in range(5):
    >>>    print(i)</code></pre>
    >>>    </body>
    >>>    </html>)
    ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    code_list = []

    # 查找所有的 <pre> 标签
    pre_tags = soup.find_all('pre')

    for pre_tag in pre_tags:
        # 检查 <pre> 标签内是否有 <code> 标签
        code_tag = pre_tag.find('code')
        if code_tag:
            # 如果有 <code> 标签，提取其文本内容
            code_text = code_tag.get_text()
        else:
            # 如果没有 <code> 标签，直接提取 <pre> 标签的文本内容
            code_text = pre_tag.get_text()

        code_list.append(code_text)

    return code_list