def text2int(self, textnum):
    """
        将单词字符串转换为相应的整数字符串
        :param textnum: 字符串，要转换的单词字符串
        :return: 字符串，最终转换的整数字符串
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    if not self.is_valid_input(textnum):
        return ''
    textnum = textnum.lower().replace('-', ' ')
    words = textnum.split()
    current = 0
    result = 0
    for word in words:
        if word in self.ordinal_words:
            current += self.ordinal_words[word]
        else:
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    word = word[:-len(ending)] + replacement
                    break
            if word not in self.numwords:
                continue
            scale, increment = self.numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
    result += current
    return str(result)