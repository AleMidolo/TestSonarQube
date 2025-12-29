def text2int(self, textnum):
    """
        将单词字符串转换为相应的整数字符串
        :param textnum: 字符串，要转换的单词字符串
        :return: 字符串，最终转换的整数字符串
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    textnum = textnum.replace('-', ' ')
    for ordinal, value in self.ordinal_words.items():
        if ordinal in textnum:
            textnum = textnum.replace(ordinal, self.units[value])
    for ending, replacement in self.ordinal_endings:
        words = textnum.split()
        new_words = []
        for word in words:
            if word.endswith(ending):
                word = '%s%s' % (word[:-len(ending)], replacement)
            new_words.append(word)
        textnum = ' '.join(new_words)
    words = [word.lower() for word in textnum.split() if word]
    current = 0
    result = 0
    for word in words:
        if word not in self.numwords:
            continue
        scale, increment = self.numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    result += current
    return str(result)