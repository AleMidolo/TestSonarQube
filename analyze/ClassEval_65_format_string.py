def format_string(self, x):
    """
        将数字的字符串表示转换为单词格式
        :param x: str，数字的字符串表示
        :return: str，数字的单词格式
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
    else:
        integer_words = self._format_integer_part(x)
        if integer_words:
            return f'{integer_words} ONLY'
        else:
            return 'ZERO ONLY'