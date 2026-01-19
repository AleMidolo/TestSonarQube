def trans_three(self, s):
    """
        Convierte un número de tres dígitos en formato de palabras
        :param s: str, el número de tres dígitos
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "UNO CIENTO Y VEINTE TRES"
        """
    s = s.zfill(3)
    result = ''
    if s[0] != '0':
        result += self.NUMBER[int(s[0])] + ' HUNDRED'
        if s[1:] != '00':
            result += ' AND '
    if s[1:] != '00':
        result += self.trans_two(s[1:])
    return result.strip()