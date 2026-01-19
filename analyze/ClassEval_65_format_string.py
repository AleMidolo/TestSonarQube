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
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        if temp:
            groups.insert(0, temp)
        group_words = []
        for i, group in enumerate(groups):
            if group == '000':
                continue
            group_num = int(group)
            if group_num == 0:
                continue
            group_str = group.zfill(3)
            words = self.trans_three(group_str)
            magnitude_index = len(groups) - i - 1
            if magnitude_index > 0 and words:
                magnitude_word = self.parse_more(magnitude_index)
                if magnitude_word:
                    words += ' ' + magnitude_word
            group_words.append(words)
        integer_words = ' '.join(group_words)
    decimal_words = ''
    if decimal_part:
        decimal_words = ' AND '
        digit_words = []
        for digit in decimal_part:
            if digit == '0':
                digit_words.append('ZERO')
            else:
                digit_words.append(self.NUMBER[int(digit)])
        decimal_words += ' '.join(digit_words)
        decimal_words += ' CENTS'
    result = integer_words + decimal_words + ' ONLY'
    if is_negative:
        result = 'MINUS ' + result
    return result