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
        while len(integer_part) > 0:
            groups.append(integer_part[-3:])
            integer_part = integer_part[:-3]
        groups.reverse()
        group_words = []
        for i, group in enumerate(groups):
            if group != '000':
                group_num = int(group)
                if group_num > 0:
                    words = self.trans_three(group.zfill(3))
                    magnitude = self.parse_more(len(groups) - i - 1)
                    if magnitude:
                        words += ' ' + magnitude
                    group_words.append(words)
        integer_words = ' '.join(group_words)
    decimal_words = ''
    if decimal_part:
        decimal_words = ' AND '
        if len(decimal_part) == 1:
            decimal_part += '0'
        decimal_words += self.trans_two(decimal_part.zfill(2))
        decimal_words += ' CENTS'
    result = ''
    if is_negative:
        result += 'MINUS '
    result += integer_words
    result += decimal_words
    result += ' ONLY'
    return result