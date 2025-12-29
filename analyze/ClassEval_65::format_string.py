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
        is_negative = x[0] == '-'
        x = x[1:]
    parts = x.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    integer_words = self._format_integer_part(integer_part)
    if decimal_part:
        decimal_words = self._format_decimal_part(decimal_part)
        result = f'{integer_words} AND {decimal_words} ONLY'
    else:
        result = f'{integer_words} ONLY'
    if is_negative:
        result = f'NEGATIVE {result}'
    return result