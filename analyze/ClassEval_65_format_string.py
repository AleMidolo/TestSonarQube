def format_string(self, x):
    """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
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
    if length > 3:
        for i in range(length, 0, -3):
            part = whole_part[max(0, i - 3):i]
            if part != '000':
                words.append(self.trans_three(part) + ' ' + self.parse_more((length - i) // 3))
    if not words:
        words.append('ZERO')
    words.reverse()
    result = ' AND '.join(words).strip()
    if decimal_part:
        result += ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part))
    return result + ' ONLY'