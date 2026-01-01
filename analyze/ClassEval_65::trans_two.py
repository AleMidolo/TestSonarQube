def trans_two(self, s):
    """
        Converte un numero a due cifre nella sua rappresentazione in parole.
        :param s: str, il numero a due cifre
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
    if not s or s == '00':
        return ''
    if len(s) == 1:
        return self.NUMBER[int(s)] if s != '0' else ''
    if s[0] == '0':
        return self.NUMBER[int(s[1])] if s[1] != '0' else ''
    if s[0] == '1':
        return self.NUMBER_TEEN[int(s[1])]
    else:
        ten_part = self.NUMBER_TEN[int(s[0]) - 1]
        one_part = self.NUMBER[int(s[1])] if s[1] != '0' else ''
        return f'{ten_part} {one_part}'.strip()