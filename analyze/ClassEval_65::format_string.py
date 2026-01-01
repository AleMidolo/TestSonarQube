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
    x = x.split('.')
    whole_part = x[0]
    decimal_part = x[1] if len(x) > 1 else ''
    words = []
    length = len(whole_part)
    if length > 0:
        for i in range(length, 0, -3):
            part = whole_part[max(0, i - 3):i]
            if part:
                words.append(self.trans_three(part) + (' ' + self.parse_more((length - i) // 3) if (length - i) // 3 < len(self.NUMBER_MORE) else ''))
    result = ' AND '.join(reversed(words)).strip()
    if decimal_part:
        result += ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part))
    return result + ' ONLY'