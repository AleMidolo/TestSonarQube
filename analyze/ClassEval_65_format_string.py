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
    result = []
    index = 0
    while n > 0:
        part = x[max(0, n - 3):n]
        if part:
            if index > 0:
                result.append(self.parse_more(index))
            if len(part) == 3:
                result.append(self.trans_three(part))
            elif len(part) == 2:
                result.append(self.trans_two(part))
            else:
                result.append(self.NUMBER[int(part)])
        n -= 3
        index += 1
    result.reverse()
    return ' AND '.join(result) + ' ONLY'