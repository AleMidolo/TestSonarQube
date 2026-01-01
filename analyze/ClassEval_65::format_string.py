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
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        groups.insert(0, temp)
        integer_words_parts = []
        for i, group in enumerate(reversed(groups)):
            group_words = self.trans_three(group.zfill(3))
            if group_words and group_words != '' and (group != '000'):
                if i > 0:
                    suffix = self.parse_more(i)
                    if suffix:
                        group_words += ' ' + suffix
                integer_words_parts.insert(0, group_words)
        integer_words = ' '.join(integer_words_parts)
    decimal_words = ''
    if decimal_part:
        decimal_words = ' AND '
        if len(decimal_part) == 1:
            decimal_words += self.trans_two(decimal_part + '0')
        else:
            decimal_words += self.trans_two(decimal_part[:2].zfill(2))
        if len(decimal_part) > 2:
            decimal_words += ' ' + ' '.join([self.NUMBER[int(d)] for d in decimal_part[2:] if d != '0'])
        decimal_words += ' CENTS'
    result = ''
    if is_negative:
        result += 'MINUS '
    result += integer_words
    if decimal_words:
        result += decimal_words
    result += ' ONLY'
    return result