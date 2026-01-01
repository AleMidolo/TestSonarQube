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
    if length > 0:
        for i in range(length):
            if length - i > 3:
                words.append(self.trans_three(whole_part[i:i + 3]))
                if (length - i - 3) // 3 >= 0:
                    words.append(self.parse_more((length - i - 3) // 3))
            elif length - i == 3:
                words.append(self.trans_three(whole_part[i:i + 3]))
            elif length - i == 2:
                words.append(self.trans_two(whole_part[i:i + 2]))
            elif length - i == 1:
                words.append(self.NUMBER[int(whole_part[i])])
    result = ' AND '.join(filter(None, words)).strip()
    if decimal_part:
        result += ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part if digit.isdigit()))
    return result + ' ONLY' if result else ''