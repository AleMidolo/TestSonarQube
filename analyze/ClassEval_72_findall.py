def findall(self, pattern, text):
    """
    查找所有匹配的子字符串并返回所有匹配子字符串的列表
    :param pattern: 字符串，正则表达式模式
    :param text: 字符串，要匹配的文本
    :return: 字符串列表，所有匹配子字符串的列表
    >>> ru = RegexUtils()
    >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['123-456-7890', '876-286-9876', '987-762-9767']
    """
    return re.findall(pattern, text)