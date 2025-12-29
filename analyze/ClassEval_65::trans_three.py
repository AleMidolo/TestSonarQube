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
    hundreds = self.NUMBER[int(s[0])]
    tens_and_units = self.trans_two(s[1:])
    if hundreds:
        return f'{hundreds} HUNDRED' + (f' AND {tens_and_units}' if tens_and_units else '')
    else:
        return tens_and_units