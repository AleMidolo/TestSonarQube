def trans_three(self, s):
    """
        Converte un numero di tre cifre nella sua rappresentazione in parole.
        :param s: str, il numero di tre cifre
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
    s = s.zfill(3)
    if s[0] != '0':
        return self.NUMBER[int(s[0])] + ' HUNDRED' + (' AND ' + self.trans_two(s[1:]) if s[1:] != '00' else '')
    else:
        return self.trans_two(s[1:])