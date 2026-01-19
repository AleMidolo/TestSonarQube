import re

def split(self, pattern, text):
    """
    根据正则表达式模式拆分文本并返回子字符串列表
    :param pattern: 字符串,正则表达式模式
    :param text: 字符串,待拆分的文本
    :return: 字符串列表,拆分后的子字符串列表
    >>> ru = RegexUtils()
    >>> ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['', ' abiguygusu ', ' kjgufwycs ', '']
    """
    return re.split(pattern, text)