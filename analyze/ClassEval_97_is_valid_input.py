def is_valid_input(self, textnum):
    """
        检查输入文本是否仅包含可以转换为数字的有效单词。
        :param textnum: 包含表示数字的单词的输入文本。
        :return: 如果输入有效则返回 True，否则返回 False。
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    textnum = textnum.replace('-', ' ')
    words = textnum.split()
    if not words:
        return False
    for word in words:
        if word in self.ordinal_words:
            continue
        is_ordinal = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
                if base_word in self.numwords:
                    is_ordinal = True
                    break
        if is_ordinal:
            continue
        if word not in self.numwords:
            return False
    return True