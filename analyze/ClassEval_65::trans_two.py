def trans_two(self, s):
    """
        दो अंकों की संख्या को शब्दों के प्रारूप में परिवर्तित करता है
        :param s: str, दो अंकों की संख्या
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
    if not s or s == '00':
        return ''
    if len(s) == 1:
        return self.NUMBER[int(s)] if s != '0' else ''
    if s[0] == '0':
        return self.NUMBER[int(s[1])] if s[1] != '0' else ''
    if s[0] == '1':
        return self.NUMBER_TEEN[int(s[1])]
    else:
        ten_part = self.NUMBER_TEN[int(s[0]) - 1]
        one_part = self.NUMBER[int(s[1])] if s[1] != '0' else ''
        return f'{ten_part} {one_part}'.strip()