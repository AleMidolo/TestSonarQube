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
    num = int(s)
    if num < 10:
        return self.NUMBER[num]
    elif 10 <= num < 20:
        return self.NUMBER_TEEN[num - 10]
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return self.NUMBER_TEN[tens_digit - 1]
        else:
            return f'{self.NUMBER_TEN[tens_digit - 1]} {self.NUMBER[ones_digit]}'