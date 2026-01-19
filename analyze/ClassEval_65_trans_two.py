def trans_two(self, s):
    """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
    if not s or s == '00':
        return ''
    if len(s) == 1:
        s = '0' + s
    if s[0] == '0':
        return self.NUMBER[int(s[1])]
    elif s[0] == '1':
        return self.NUMBER_TEEN[int(s[1])]
    elif s[1] == '0':
        return self.NUMBER_TEN[int(s[0]) - 1]
    else:
        return f'{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}'