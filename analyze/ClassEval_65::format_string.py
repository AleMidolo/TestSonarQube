def format_string(self, x):
    """
        Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
        :param x: str, la rappresentazione stringa di un numero
        :return: str, il numero nel formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if not x.isdigit():
        return ''
    x = int(x)
    if x == 0:
        return 'ZERO ONLY'
    words = []
    if x < 0:
        words.append('MINUS')
        x = -x
    thousands = ['', 'THOUSAND', 'MILLION', 'BILLION']
    i = 0
    while x > 0:
        if x % 1000 != 0:
            words.append(self.trans_three(str(x % 1000).zfill(3)) + (' ' + thousands[i] if thousands[i] else ''))
        x //= 1000
        i += 1
    words.reverse()
    return ' '.join(words).strip() + ' ONLY'