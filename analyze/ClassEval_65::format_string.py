def format_string(self, x):
    """
        एक संख्या के स्ट्रिंग प्रतिनिधित्व को शब्दों के प्रारूप में परिवर्तित करता है
        :param x: str, संख्या का स्ट्रिंग प्रतिनिधित्व
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "एक सौ और तेईस हजार चार सौ और छप्पन केवल"
        """
    if '.' in x:
        integer_part, decimal_part = x.split('.')
    else:
        integer_part = x
        decimal_part = ''
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    result_parts = []
    integer_part_len = len(integer_part)
    if integer_part_len == 1 and integer_part[0] == '0':
        result_parts.append('ZERO')
    else:
        groups = []
        for i in range(integer_part_len, 0, -3):
            start = max(0, i - 3)
            groups.append(integer_part[start:i])
        groups.reverse()
        for i, group in enumerate(groups):
            group_index = len(groups) - 1 - i
            if group != '000':
                words = self.trans_three(group.zfill(3))
                if words:
                    suffix = self.parse_more(group_index)
                    if suffix:
                        words += ' ' + suffix
                    result_parts.append(words)
    result = ' '.join(result_parts).strip()
    if decimal_part:
        decimal_part = decimal_part[:2]
        if decimal_part:
            decimal_words = self.trans_two(decimal_part.zfill(2))
            if decimal_words:
                result += ' AND CENTS ' + decimal_words
    if result:
        result += ' ONLY'
    return result