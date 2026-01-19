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
        if textnum.endswith(ending):
            textnum = textnum[:-len(ending)] + replacement
    words = textnum.lower().split()
    current = 0
    result = 0
    for word in words:
        if word == 'and':
            continue
        if word not in self.numwords:
            if word in self.tens:
                continue
            else:
                for i in range(len(word) - 1, 0, -1):
                    if word[:i] in self.numwords and word[i:] in self.numwords:
                        scale1, increment1 = self.numwords[word[:i]]
                        scale2, increment2 = self.numwords[word[i:]]
                        current = current * scale1 + increment1
                        current += increment2
                        break
                else:
                    continue
        else:
            scale, increment = self.numwords[word]
            if scale > 100:
                result += current * scale
                current = 0
            else:
                current = current * scale + increment
            if scale > current:
                result += current
                current = 0
    result += current
    return str(result)