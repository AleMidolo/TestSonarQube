def trans_two(self, s):
    """
        Converte un numero a due cifre nella sua rappresentazione in parole.
        :param s: str, il numero a due cifre
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
    if len(s) == 0 or s == '00':
        return ''
    if s[0] == '0':
        return self.NUMBER[int(s[1])] if s[1] != '0' else ''
    if s[0] == '1':
        return self.NUMBER_TEEN[int(s[1])]
    if s[1] == '0':
        return self.NUMBER_TEN[int(s[0]) - 1]
    return f'{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}'