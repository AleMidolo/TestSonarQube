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
    for i in range(length):
        if length - i - 1 > 2:
            part = whole_part[max(0, length - i - 3):length - i]
            if part:
                words.append(self.trans_three(part))
                words.append(self.parse_more((length - i - 1) // 3))
        elif length - i - 1 == 2:
            part = whole_part[max(0, length - i - 3):length - i]
            if part:
                words.append(self.trans_three(part))
        elif length - i - 1 == 1:
            part = whole_part[max(0, length - i - 2):length - i]
            if part:
                words.append(self.trans_two(part))
        elif length - i - 1 == 0:
            part = whole_part[max(0, length - i - 1):length - i]
            if part:
                words.append(self.NUMBER[int(part)])
    result = ' AND '.join(words).strip()
    if decimal_part:
        result += ' POINT ' + ' '.join((self.NUMBER[int(digit)] for digit in decimal_part))
    return result + ' ONLY' if result else ''