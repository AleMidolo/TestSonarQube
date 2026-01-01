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
    if s[0] == '0':
        return self.trans_two(s[1:])
    elif s[1:] == '00':
        return self.NUMBER[int(s[0])] + ' HUNDRED'
    else:
        return self.NUMBER[int(s[0])] + ' HUNDRED AND ' + self.trans_two(s[1:])