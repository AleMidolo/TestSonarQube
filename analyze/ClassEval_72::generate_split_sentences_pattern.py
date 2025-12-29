def generate_split_sentences_pattern(self):
    """
        生成匹配两个句子中间字符的正则表达式模式
        :return: 字符串，匹配两个句子中间字符的正则表达式模式
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\\s]{1,2}(?=[A-Z])'
        """
    pattern = '[.!?][\\s]{1,2}(?=[A-Z])'
    return pattern