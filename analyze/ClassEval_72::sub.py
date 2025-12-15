def sub(self, pattern, replacement, text):
        """
        用指定的字符串替换正则表达式匹配的子字符串
        :param pattern: 字符串, 正则表达式模式
        :param replacement: 替换用的文本
        :param text: 字符串, 要被替换的文本
        :return: 字符串, 替换后的文本
        >>> ru = RegexUtils()
        >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        'phone num abiguygusu phone num kjgufwycs phone num'
        """
        return re.sub(pattern, replacement, text)