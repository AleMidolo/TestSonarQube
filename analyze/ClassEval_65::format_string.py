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
        decimal_part = decimal_part[:2]
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    if integer_part == '0':
        result = 'ZERO'
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
                    magnitude = self.parse_more(len(groups) - i - 1)
                    if magnitude:
                        word += ' ' + magnitude
                    group_words.append(word)
        result = ' '.join(group_words)
    if is_negative:
        result = 'MINUS ' + result
    if decimal_part:
        decimal_part = decimal_part.lstrip('0')
        if decimal_part:
            decimal_words = []
            for digit in decimal_part:
                if digit != '0':
                    decimal_words.append(self.NUMBER[int(digit)])
                else:
                    decimal_words.append('ZERO')
            result += ' AND ' + ' '.join(decimal_words) + ' CENTS'
    result += ' ONLY'
    return result