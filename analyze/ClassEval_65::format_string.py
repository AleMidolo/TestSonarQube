def format_string(self, x):
    """
        Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
        :param x: str, la rappresentazione stringa di un numero
        :return: str, il numero nel formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "UNO CENTO E VENTITRE MILA QUATTROCENTO E CINQUANTA SEI SOLO"
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
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    if integer_part == '0':
        integer_words = 'ZERO'
    else:
        groups = []
        temp = integer_part
        while len(temp) > 3:
            groups.append(temp[-3:])
            temp = temp[:-3]
        groups.append(temp)
        groups.reverse()
        integer_words_parts = []
        for i, group in enumerate(groups):
            if group != '000':
                group_words = self.trans_three(group.zfill(3))
                magnitude = self.parse_more(len(groups) - i - 1)
                if magnitude:
                    group_words += ' ' + magnitude
                integer_words_parts.append(group_words)
        integer_words = ' '.join(integer_words_parts)
    decimal_words = ''
    if decimal_part:
        decimal_words = ' AND '
        decimal_digits = []
        for digit in decimal_part:
            if digit == '0':
                decimal_digits.append('ZERO')
            else:
                decimal_digits.append(self.NUMBER[int(digit)])
        decimal_words += ' '.join(decimal_digits) + ' CENTS'
    result = ''
    if is_negative:
        result += 'MINUS '
    result += integer_words
    if decimal_words:
        result += decimal_words
    result += ' ONLY'
    return result