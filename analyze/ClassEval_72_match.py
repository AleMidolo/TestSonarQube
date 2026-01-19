def match(self, pattern, text):
    """
    检查文本是否与正则表达式匹配
    :param pattern: 字符串,正则表达式模式
    :param text: 字符串,要匹配的文本
    :return: True 或 False,表示文本是否与正则表达式匹配
    >>> ru = RegexUtils()
    >>> ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
    True
    """
    import re
    return bool(re.search(pattern, text))