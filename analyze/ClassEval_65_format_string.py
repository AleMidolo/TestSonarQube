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
    thousands = ['', 'THOUSAND', 'MILLION', 'BILLION']
    index = 0
    while x > 0:
        part = x % 1000
        if part > 0:
            words_part = self.trans_three(str(part).zfill(3))
            if thousands[index]:
                words_part += ' ' + thousands[index]
            words.append(words_part)
        x //= 1000
        index += 1
    return ' AND '.join(reversed(words)).strip() + ' ONLY'