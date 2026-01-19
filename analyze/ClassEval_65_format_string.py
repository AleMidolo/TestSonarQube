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
            if group == '000':
                continue
            group_words = ''
            if len(group) == 3:
                group_words = self.trans_three(group)
            elif len(group) == 2:
                group_words = self.trans_two(group)
            else:
                group_words = self.NUMBER[int(group)]
            magnitude_index = len(groups) - i - 1
            if magnitude_index > 0 and group_words:
                magnitude_word = self.parse_more(magnitude_index)
                if magnitude_word:
                    group_words += ' ' + magnitude_word
            if group_words:
                result_parts.append(group_words)
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            result_parts.append('AND')
            decimal_words = []
            for digit in decimal_part:
                decimal_words.append(self.NUMBER[int(digit)])
            result_parts.append(' '.join(decimal_words))
            result_parts.append('CENTS')
    result_parts.append('ONLY')
    if is_negative:
        result_parts.insert(0, 'MINUS')
    result = ' '.join(result_parts)
    result = ' '.join(result.split())
    return result