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
    n = int(x)
    if n == 0:
        return 'ZERO ONLY'
    words = []
    if n < 0:
        words.append('MINUS')
        n = -n
    thousands = ['', 'THOUSAND', 'MILLION', 'BILLION']
    idx = 0
    while n > 0:
        part = n % 1000
        if part > 0:
            if part < 100:
                words.append(self.trans_two(str(part).zfill(2)))
            else:
                words.append(self.trans_three(str(part).zfill(3)))
            if idx > 0:
                words.append(thousands[idx])
        n //= 1000
        idx += 1
    words.reverse()
    return ' '.join(words) + ' ONLY'