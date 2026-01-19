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
    chunks = []
    while n > 0:
        chunks.append(n % 1000)
        n //= 1000
    for i in range(len(chunks)):
        if chunks[i] > 0:
            words.append(self.trans_three(str(chunks[i]).zfill(3)))
            if i > 0:
                words.append(self.parse_more(i))
    return ' '.join(reversed(words)) + ' ONLY'