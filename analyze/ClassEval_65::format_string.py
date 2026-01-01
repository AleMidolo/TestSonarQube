def format_string(self, x):
    """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
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
    integer_words = self._format_integer_part(integer_part)
    if decimal_part:
        decimal_words = self._format_decimal_part(decimal_part)
        result = f'{integer_words} AND {decimal_words} ONLY'
    else:
        result = f'{integer_words} ONLY'
    if is_negative:
        result = f'NEGATIVE {result}'
    return result