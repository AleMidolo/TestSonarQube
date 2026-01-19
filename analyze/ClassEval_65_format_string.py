def format_string(self, x):
    """
        Convierte una representación de cadena de un número en formato de palabras
        :param x: str, la representación de cadena de un número
        :return: str, el número en formato de palabras
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
    return ' AND '.join(reversed(words)).strip() + ' ONLY'