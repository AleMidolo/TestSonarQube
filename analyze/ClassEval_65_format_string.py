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
    integer_words = []
    if integer_part == '0':
        integer_words.append('ZERO')
    else:
        groups = []
        temp = integer_part
        while len(temp) > 3:
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        groups.insert(0, temp)
        for i, group in enumerate(groups):
            group_words = self.trans_three(group.zfill(3))
            if group_words.strip():
                magnitude = len(groups) - i - 1
                if magnitude > 0 and self.parse_more(magnitude):
                    integer_words.append(group_words + ' ' + self.parse_more(magnitude))
                else:
                    integer_words.append(group_words)
    decimal_words = []
    if decimal_part:
        decimal_part = decimal_part[:2]
        if decimal_part:
            decimal_words.append('AND CENTS ' + self.trans_two(decimal_part.zfill(2)))
    result_parts = []
    if is_negative:
        result_parts.append('MINUS')
    result_parts.extend(integer_words)
    result_parts.extend(decimal_words)
    if not decimal_part:
        result_parts.append('ONLY')
    return ' '.join(filter(None, result_parts))