def trans_three(self, s):
    """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
    s = s.zfill(3)
    result = ''
    if s[0] != '0':
        result += self.NUMBER[int(s[0])] + ' HUNDRED'
        if s[1:] != '00':
            result += ' AND '
    if s[1:] != '00':
        result += self.trans_two(s[1:])
    return result.strip()