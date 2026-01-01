def trans_three(self, s):
    """
        तीन अंकों की संख्या को शब्दों के प्रारूप में परिवर्तित करता है
        :param s: str, तीन अंकों की संख्या
        :return: str, संख्या शब्दों के प्रारूप में
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