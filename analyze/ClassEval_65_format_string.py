def format_string(self, x):
    """
        Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
        :param x: str, la rappresentazione stringa di un numero
        :return: str, il numero nel formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "UNO CENTO E VENTITRE MILA QUATTROCENTO E CINQUANTA SEI SOLO"
        """
    if not x:
        return ''
    is_negative = False
    if x[0] == '-':
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
        while len(integer_part) > 0:
            groups.append(integer_part[-3:])
            integer_part = integer_part[:-3]
        groups.reverse()
        for i, group in enumerate(groups):
            if group == '000':
                continue
            group_words = []
            if len(group) == 3:
                group_words.append(self.trans_three(group))
            elif len(group) == 2:
                group_words.append(self.trans_two(group))
            else:
                group_words.append(self.NUMBER[int(group)])
            magnitude_index = len(groups) - i - 1
            if magnitude_index > 0 and group != '000':
                suffix = self.parse_more(magnitude_index)
                if suffix:
                    group_words.append(suffix)
            integer_words.extend(group_words)
    decimal_words = []
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_words.append('AND')
            for digit in decimal_part:
                if digit == '0':
                    decimal_words.append('ZERO')
                else:
                    decimal_words.append(self.NUMBER[int(digit)])
            decimal_words.append('CENTS')
    result_parts = []
    if is_negative:
        result_parts.append('MINUS')
    result_parts.extend(integer_words)
    result_parts.extend(decimal_words)
    result_parts.append('ONLY')
    result = ' '.join(filter(None, result_parts))
    return result