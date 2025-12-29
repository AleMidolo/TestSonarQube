def format_string(self, x):
    """
        将数字的字符串表示转换为单词格式
        :param x: str，数字的字符串表示
        :return: str，数字的单词格式
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if not x:
        return ''
    is_negative = False
    if x[0] == '-':
        is_negative = True
        x = x[1:]
    integer_part = x
    decimal_part = ''
    if '.' in x:
        integer_part, decimal_part = x.split('.')
        decimal_part = decimal_part.rstrip('0')
    if integer_part == '0':
        result = 'ZERO'
    else:
        integer_part = integer_part.lstrip('0')
        if not integer_part:
            integer_part = '0'
        groups = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            groups.append(integer_part[start:i])
        groups.reverse()
        group_words = []
        for i, group in enumerate(groups):
            if group == '000':
                continue
            group_index = len(groups) - i - 1
            if len(group) == 3:
                words = self.trans_three(group)
            elif len(group) == 2:
                words = self.trans_two(group)
            else:
                words = self.trans_two('0' + group)
            if words and group_index > 0:
                suffix = self.parse_more(group_index)
                if suffix:
                    words += ' ' + suffix
            if words:
                group_words.append(words)
        result = ' '.join(group_words)
    if decimal_part:
        decimal_words = []
        for digit in decimal_part:
            if digit == '0':
                decimal_words.append('ZERO')
            else:
                decimal_words.append(self.NUMBER[int(digit)])
        result += ' AND CENTS ' + ' '.join(decimal_words)
    if is_negative:
        result = 'MINUS ' + result
    if result:
        result += ' ONLY'
    return result