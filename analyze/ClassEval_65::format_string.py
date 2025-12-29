def format_string(self, x):
    """
        एक संख्या के स्ट्रिंग प्रतिनिधित्व को शब्दों के प्रारूप में परिवर्तित करता है
        :param x: str, संख्या का स्ट्रिंग प्रतिनिधित्व
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "एक सौ और तेईस हजार चार सौ और छप्पन केवल"
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
        integer_part, decimal_part = x.split('.', 1)
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    if integer_part == '0':
        result = 'ZERO'
    else:
        groups = []
        temp = integer_part
        while temp:
            groups.append(temp[-3:])
            temp = temp[:-3] if len(temp) > 3 else ''
        groups.reverse()
        words = []
        for i, group in enumerate(groups):
            if group != '000':
                group_words = self.trans_three(group.zfill(3))
                magnitude = self.parse_more(len(groups) - i - 1)
                if group_words:
                    if magnitude:
                        words.append(f'{group_words} {magnitude}')
                    else:
                        words.append(group_words)
        result = ' '.join(words)
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_words = []
            for digit in decimal_part:
                if digit != '0':
                    decimal_words.append(self.NUMBER[int(digit)])
                else:
                    decimal_words.append('ZERO')
            result += f" AND {', '.join(decimal_words)} CENTS"
    if is_negative:
        result = f'NEGATIVE {result}'
    result += ' ONLY'
    return result