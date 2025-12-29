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
        temp = integer_part
        while len(temp) > 3:
            groups.insert(0, temp[-3:])
            temp = temp[:-3]
        if temp:
            groups.insert(0, temp)
        for i, group in enumerate(groups):
            group_words = []
            if len(group) == 3:
                group_words.append(self.trans_three(group))
            elif len(group) == 2:
                group_words.append(self.trans_two(group))
            elif len(group) == 1:
                if group != '0':
                    group_words.append(self.NUMBER[int(group)])
            if group_words and group_words[0] != '':
                magnitude_index = len(groups) - i - 1
                if magnitude_index > 0 and group != '000':
                    group_words.append(self.parse_more(magnitude_index))
                integer_words.extend(group_words)
    decimal_words = []
    if decimal_part:
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_words.append('AND')
            if len(decimal_part) == 1:
                decimal_words.append(f'{self.NUMBER[int(decimal_part[0])]} CENTS')
            elif len(decimal_part) == 2:
                decimal_words.append(f'{self.trans_two(decimal_part)} CENTS')
            else:
                cents_digits = []
                for digit in decimal_part:
                    if digit != '0':
                        cents_digits.append(self.NUMBER[int(digit)])
                if cents_digits:
                    decimal_words.append(' '.join(cents_digits) + ' CENTS')
    result_parts = []
    if is_negative:
        result_parts.append('MINUS')
    if integer_words:
        result_parts.extend(integer_words)
    if decimal_words:
        result_parts.extend(decimal_words)
    if result_parts:
        result_parts.append('ONLY')
    return ' '.join(result_parts).strip()