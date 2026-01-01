def format_string(self, x):
    """
        将数字的字符串表示转换为单词格式
        :param x: str，数字的字符串表示
        :return: str，数字的单词格式
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    is_negative = False
    if x.startswith('-'):
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
        temp = integer_part
        while len(temp) > 3:
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        groups.insert(0, temp)
        group_words = []
        for i, group in enumerate(groups):
            if group != '000':
                group_word = self.trans_three(group.zfill(3))
                magnitude = len(groups) - i - 1
                if magnitude > 0 and group_word:
                    group_word += ' ' + self.parse_more(magnitude)
                if group_word:
                    group_words.append(group_word)
        result = ' '.join(group_words)
    if decimal_part:
        decimal_words = []
        for digit in decimal_part:
            if digit == '0':
                decimal_words.append('ZERO')
            else:
                decimal_words.append(self.NUMBER[int(digit)])
        result += ' POINT ' + ' '.join(decimal_words)
    if is_negative:
        result = 'MINUS ' + result
    if not decimal_part:
        result += ' ONLY'
    return result