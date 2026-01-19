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
        s = '0' + s
    num = int(s)
    if num == 0:
        return ''
    elif num < 10:
        return self.NUMBER[num]
    elif num < 20:
        return self.NUMBER_TEEN[num - 10]
    else:
        tens_digit = int(s[0])
        ones_digit = int(s[1])
        if ones_digit == 0:
            return self.NUMBER_TEN[tens_digit - 1]
        else:
            return f'{self.NUMBER_TEN[tens_digit - 1]} {self.NUMBER[ones_digit]}'