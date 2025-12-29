def format_string(self, x):
    """
        将数字的字符串表示转换为单词格式
        :param x: str，数字的字符串表示
        :return: str，数字的单词格式
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if not x.isdigit():
        return ''
    x = x.split('.')[0]
    n = len(x)
    if n == 0:
        return 'ZERO ONLY'
    words = []
    index = 0
    while n > 0:
        n_part = x[max(0, n - 3):n]
        if n_part:
            if index > 0:
                words.append(self.parse_more(index))
            if len(n_part) == 3:
                words.append(self.trans_three(n_part))
            elif len(n_part) == 2:
                words.append(self.trans_two(n_part))
            elif len(n_part) == 1:
                words.append(self.NUMBER[int(n_part)])
        n -= 3
        index += 1
    words.reverse()
    result = ' AND '.join(words).strip()
    return result + ' ONLY'