def format(self, x):
        """
        एक संख्या को शब्दों के प्रारूप में परिवर्तित करता है
        :param x: int या float, वह संख्या जिसे शब्दों के प्रारूप में परिवर्तित किया जाना है
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        return self.format_string(str(int(x))) if isinstance(x, (int, float)) else ""