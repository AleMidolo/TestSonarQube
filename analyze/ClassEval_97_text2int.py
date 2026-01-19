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
        raise ValueError('Invalid input')
    textnum = textnum.replace('-', ' ')
    current = result = 0
    for word in textnum.split():
        if word in self.numwords:
            scale, increment = self.numwords[word]
            current += increment
            if scale > 1:
                current *= scale
                result += current
                current = 0
        elif word == 'and':
            continue
    return str(result + current)