import re

def extract_email(self, text):
    """
    पाठ से सभी ईमेल पते निकालें
    :param text: स्ट्रिंग, इनपुट पाठ
    :return: स्ट्रिंग की सूची, सभी निकाले गए ईमेल पते
    >>> ru = RegexUtils()
    >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
    ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)