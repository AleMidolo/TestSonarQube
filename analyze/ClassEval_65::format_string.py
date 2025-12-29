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
    x = x.split('.')
    whole_part = x[0]
    decimal_part = x[1] if len(x) > 1 else ''
    words = []
    length = len(whole_part)
    if length == 0:
        return 'ZERO ONLY'
    for i in range(length, 0, -3):
        group = whole_part[max(0, i - 3):i]
        if group:
            group_words = self.trans_three(group)
            if i // 3 > 0:
                group_words += ' ' + self.parse_more(i // 3)
            words.append(group_words)
    words.reverse()
    result = ' AND '.join(words).strip()
    if decimal_part:
        result += ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part))
    return result + ' ONLY'