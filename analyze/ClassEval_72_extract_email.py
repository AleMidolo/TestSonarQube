import re

def extract_email(self, text):
    """
    Estrae tutti gli indirizzi email dal testo
    :param text: stringa, testo di input
    :return: lista di stringhe, tutti gli indirizzi email estratti
    >>> ru = RegexUtils()
    >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
    ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)