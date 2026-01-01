def generate_phone_number_pattern(self):
    """
        生成匹配电话号码的正则表达式模式
        :return: 字符串，匹配电话号码的正则表达式模式
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\x08\\d{3}-\\d{3}-\\d{4}\x08'
        """
    pattern = '\\b\\d{3}-\\d{3}-\\d{4}\\b'
    return pattern