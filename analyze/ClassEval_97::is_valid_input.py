def is_valid_input(self, textnum):
    """
        检查输入文本是否仅包含可以转换为数字的有效单词。
        :param textnum: 包含表示数字的单词的输入文本。
        :return: 如果输入有效则返回 True，否则返回 False。
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    valid_words = set(self.numwords.keys()).union(self.ordinal_words.keys())
    words = textnum.replace('-', ' ').split()
    return all((word in valid_words for word in words))