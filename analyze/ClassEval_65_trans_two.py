def trans_two(self, s):
    """
        Convierte un número de dos dígitos en formato de palabras
        :param s: str, el número de dos dígitos
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "VEINTITRÉS"
        """
    if s[0] == '1':
        return self.NUMBER_TEEN[int(s[1])] if s[1] != '0' else self.NUMBER_TEN[0]
    elif s[0] == '0':
        return self.NUMBER[int(s[1])]
    else:
        return f'{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}' if s[1] != '0' else self.NUMBER_TEN[int(s[0]) - 1]