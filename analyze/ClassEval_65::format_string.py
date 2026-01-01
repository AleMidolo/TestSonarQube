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
    if integer_part == '0':
        result = 'ZERO'
    else:
        integer_part = integer_part.lstrip('0')
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
            magnitude = self.parse_more(len(groups) - i - 1)
            if group_words:
                if magnitude:
                    words.append(f'{group_words} {magnitude}')
                else:
                    words.append(group_words)
        result = ' '.join(words)
    if decimal_part:
        decimal_words = []
        for digit in decimal_part:
            if digit == '0':
                decimal_words.append('ZERO')
            else:
                decimal_words.append(self.NUMBER[int(digit)])
        result = f"{result} AND {' '.join(decimal_words)}"
    if is_negative:
        result = f'NEGATIVE {result}'
    return f'{result} ONLY'