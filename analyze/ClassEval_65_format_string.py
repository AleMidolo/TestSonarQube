def format_string(self, x):
    """
        Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
        :param x: str, la rappresentazione stringa di un numero
        :return: str, il numero nel formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    groups = []
    while len(x) > 0:
        groups.append(x[-3:])
        x = x[:-3]
    groups.reverse()
    words = []
    for i, group in enumerate(groups):
        if group != '000':
            words.append(self.trans_three(group) + (' ' + self.parse_more(len(groups) - 1 - i) if len(groups) - 1 - i > 0 else ''))
    return ' AND '.join(words).strip() + ' ONLY'