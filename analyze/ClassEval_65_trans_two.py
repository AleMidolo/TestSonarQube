def trans_two(self, s):
    """
        Convierte un número de dos dígitos en formato de palabras
        :param s: str, el número de dos dígitos
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "VEINTITRÉS"
        """
    if not s or s == '00':
        return ''
    if len(s) == 1:
        return self.NUMBER[int(s)] if s != '0' else ''
    num = int(s)
    if num < 10:
        return self.NUMBER[num]
    elif 10 <= num < 20:
        return self.NUMBER_TEEN[num - 10]
    else:
        tens = self.NUMBER_TEN[int(s[0]) - 1]
        ones = self.NUMBER[int(s[1])]
        if ones:
            return f'{tens} {ones}'
        else:
            return tens