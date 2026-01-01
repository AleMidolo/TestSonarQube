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
    parts = x.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    integer_words = []
    if integer_part == '0':
        integer_words.append('ZERO')
    else:
        groups = []
        temp = integer_part
        while len(temp) > 3:
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        groups.insert(0, temp)
        for i, group in enumerate(groups):
            group_words = self.trans_three(group.zfill(3))
            if group_words.strip():
                magnitude_index = len(groups) - i - 1
                magnitude_word = self.parse_more(magnitude_index)
                if magnitude_word:
                    integer_words.append(f'{group_words} {magnitude_word}')
                else:
                    integer_words.append(group_words)
    decimal_words = []
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_words.append('AND')
            decimal_words.append(self.trans_two(decimal_part[:2].zfill(2)))
            if len(decimal_part) > 2:
                decimal_words.append('CENTS')
    result_parts = []
    if is_negative:
        result_parts.append('MINUS')
    result_parts.extend(integer_words)
    result_parts.extend(decimal_words)
    result_parts.append('ONLY')
    result = ' '.join(result_parts)
    result = ' '.join(result.split())
    return result