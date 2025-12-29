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
        integer_part, decimal_part = x.split('.')
        decimal_part = decimal_part.rstrip('0')
    if integer_part == '0':
        result = 'ZERO'
    else:
        integer_part = integer_part.lstrip('0')
        if not integer_part:
            integer_part = '0'
        groups = []
        while integer_part:
            groups.append(integer_part[-3:])
            integer_part = integer_part[:-3]
        groups.reverse()
        words = []
        for i, group in enumerate(groups):
            if group == '000':
                continue
            group_words = self.trans_three(group.zfill(3))
            magnitude = len(groups) - i - 1
            if magnitude > 0 and group_words:
                group_words += ' ' + self.parse_more(magnitude)
            if group_words:
                words.append(group_words)
        result = ' '.join(words)
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
    if result:
        result += ' ONLY'
    return result