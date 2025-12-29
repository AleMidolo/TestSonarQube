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
    decimal_part = ''
    if '.' in x:
        integer_part, decimal_part = x.split('.')
        decimal_part = decimal_part.rstrip('0')
        if decimal_part:
            decimal_part = ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part))
        else:
            decimal_part = ''
    else:
        integer_part = x
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    if integer_part == '0':
        return 'ZERO ONLY'
    groups = []
    while integer_part:
        groups.append(integer_part[-3:])
        integer_part = integer_part[:-3]
    groups.reverse()
    words = []
    num_groups = len(groups)
    for i, group in enumerate(groups):
        if group == '000':
            continue
        group_words = self.trans_three(group.zfill(3))
        magnitude = num_groups - i - 1
        if magnitude > 0 and group_words:
            group_words += ' ' + self.parse_more(magnitude)
        words.append(group_words)
    result = ' '.join(words)
    if is_negative:
        result = 'MINUS ' + result
    if decimal_part:
        result += decimal_part
    result += ' ONLY'
    return result