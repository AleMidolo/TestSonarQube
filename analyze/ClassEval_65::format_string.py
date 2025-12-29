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
    parts = x.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    result_parts = []
    if integer_part == '0':
        result_parts.append('ZERO')
    else:
        groups = []
        temp = integer_part
        while len(temp) > 3:
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        if temp:
            groups.insert(0, temp)
        for i, group in enumerate(groups):
            group_words = self.trans_three(group.zfill(3))
            if group_words:
                magnitude = len(groups) - i - 1
                if magnitude > 0 and group_words != '':
                    group_words += ' ' + self.parse_more(magnitude)
                result_parts.append(group_words)
    result = ' '.join(result_parts)
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_words = []
            for digit in decimal_part:
                if digit != '0':
                    decimal_words.append(self.NUMBER[int(digit)])
                else:
                    decimal_words.append('ZERO')
            result += ' AND ' + ' '.join(decimal_words) + ' CENTS'
    if is_negative:
        result = 'MINUS ' + result
    if result:
        result += ' ONLY'
    return result