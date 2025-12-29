def format_string(self, x):
    """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if x.startswith('-'):
        return 'MINUS ' + self.format_string(x[1:])
    if '.' in x:
        integer_part, decimal_part = x.split('.')
        integer_words = self._format_integer_part(integer_part)
        decimal_words = self._format_decimal_part(decimal_part)
        if integer_words:
            return f'{integer_words} AND {decimal_words} ONLY'
        else:
            return f'{decimal_words} ONLY'
    integer_words = self._format_integer_part(x)
    if integer_words:
        return f'{integer_words} ONLY'
    else:
        return 'ZERO ONLY'