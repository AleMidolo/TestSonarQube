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
    decimal_part = ''
    if '.' in x:
        integer_part, decimal_part = x.split('.')
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_part = decimal_part.ljust(2, '0')[:2]
    else:
        integer_part = x
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    if integer_part == '0':
        words = 'ZERO'
    else:
        groups = []
        temp = integer_part
        while len(temp) > 3:
            groups.append(temp[-3:])
            temp = temp[:-3]
        groups.append(temp)
        groups.reverse()
        group_words = []
        for i, group in enumerate(groups):
            if group != '000':
                group_num = int(group)
                if group_num > 0:
                    word = self.trans_three(group.zfill(3))
                    magnitude = len(groups) - i - 1
                    if magnitude > 0:
                        word += ' ' + self.parse_more(magnitude)
                    group_words.append(word)
        words = ' '.join(group_words)
    if decimal_part and decimal_part != '00':
        decimal_words = self.trans_two(decimal_part.zfill(2))
        words += f' AND {decimal_words} CENTS'
    if is_negative:
        words = 'MINUS ' + words
    words += ' ONLY'
    return words