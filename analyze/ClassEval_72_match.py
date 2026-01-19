def match(self, pattern, text):
    """
        检查文本是否与正则表达式匹配
        :param pattern: 字符串，正则表达式模式
        :param text: 字符串，要匹配的文本
        :return: True 或 False，表示文本是否与正则表达式匹配
        >>> ru = RegexUtils()
        >>> ru.match(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890")
        True
        """
    match_obj = re.match(pattern, text)
    return match_obj is not None