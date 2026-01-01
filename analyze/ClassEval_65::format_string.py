def format_string(self, x):
    """
        Convierte una representación de cadena de un número en formato de palabras
        :param x: str, la representación de cadena de un número
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if not x.isdigit():
        return ''
    x = int(x)
    if x == 0:
        return 'ZERO ONLY'
    words = []
    if x < 0:
        words.append('MINUS')
        x = -x
    thousands = 0
    while x > 0:
        if x % 1000 != 0:
            words.append(self.trans_three(str(x % 1000).zfill(3)) + ' ' + self.parse_more(thousands))
        x //= 1000
        thousands += 1
    words.reverse()
    return ' '.join(words).strip() + ' ONLY'