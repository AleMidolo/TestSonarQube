def format_string(self, x):
    """
        Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
        :param x: str, la rappresentazione stringa di un numero
        :return: str, il numero nel formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    x = x[::-1]
    groups = [x[i:i + 3][::-1] for i in range(0, len(x), 3)]
    words = []
    for i, group in enumerate(groups):
        if group != '000':
            words.append(self.trans_three(group) + (' ' + self.parse_more(i) if i > 0 else ''))
    words.reverse()
    result = ' AND '.join(words).strip()
    return result + ' ONLY'