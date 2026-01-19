def format_string(self, x):
    """
        Convierte una representación de cadena de un número en formato de palabras
        :param x: str, la representación de cadena de un número
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "UNO CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
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
        group_words = []
        for i, group in enumerate(groups):
            if group != '000':
                group_word = self.trans_three(group.zfill(3))
                magnitude = self.parse_more(len(groups) - i - 1)
                if magnitude:
                    group_word += ' ' + magnitude
                group_words.append(group_word)
        integer_words = ' '.join(group_words)
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
    result += decimal_words
    result += ' ONLY'
    return result.strip()