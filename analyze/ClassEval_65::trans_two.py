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
        s = '0' + s
    num = int(s)
    if num == 0:
        return ''
    elif num < 10:
        return self.NUMBER[num]
    elif num < 20:
        return self.NUMBER_TEEN[num - 10]
    else:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return self.NUMBER_TEN[tens - 1]
        else:
            return f'{self.NUMBER_TEN[tens - 1]} {self.NUMBER[ones]}'