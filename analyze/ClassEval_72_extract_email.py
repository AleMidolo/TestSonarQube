import re

def extract_email(self, text):
    """
    Extract all email addresses from the text
    :param text: string, input text
    :return: list of string, All extracted email addresses
    >>> ru = RegexUtils()
    >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
    ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)