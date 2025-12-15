def trans_two(self, s):
        """
        दो अंकों की संख्या को शब्दों के प्रारूप में परिवर्तित करता है
        :param s: str, दो अंकों की संख्या
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        if s[0] == "1":
            return self.NUMBER_TEEN[int(s[1])]
        elif s[0] == "0":
            return self.NUMBER[int(s[1])]
        else:
            return f"{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}"