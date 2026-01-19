def generate_email_pattern(self):
    """
    生成匹配电子邮件地址的正则表达式模式
    :return: 字符串,匹配电子邮件地址的正则表达式模式
    >>> ru = RegexUtils()
    >>> ru.generate_email_pattern()
    '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    """
    return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'