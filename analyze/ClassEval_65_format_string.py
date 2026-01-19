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
    thousands = x // 1000
    if thousands > 0:
        words.append(self.trans_three(str(thousands)))
        words.append(self.parse_more(1))
    hundreds = x % 1000
    if hundreds > 0:
        words.append(self.trans_three(str(hundreds)))
    words.append('ONLY')
    return ' '.join(words).strip()