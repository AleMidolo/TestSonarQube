def trans_three(self, s):
    """
        Converte un numero di tre cifre nella sua rappresentazione in parole.
        :param s: str, il numero di tre cifre
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "UNO CENTO E VENTI TRE"
        """
    s = s.zfill(3)
    if s[0] == '0':
        return self.trans_two(s[1:])
    elif s[1:] == '00':
        return self.NUMBER[int(s[0])] + ' HUNDRED'
    else:
        return self.NUMBER[int(s[0])] + ' HUNDRED AND ' + self.trans_two(s[1:])