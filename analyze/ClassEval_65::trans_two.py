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
    if 10 <= num <= 19:
        return self.NUMBER_TEEN[num - 10]
    tens = num // 10
    ones = num % 10
    if ones == 0:
        return self.NUMBER_TEN[tens - 1]
    else:
        return f'{self.NUMBER_TEN[tens - 1]} {self.NUMBER[ones]}'