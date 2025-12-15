class NumberWordFormatter: 
    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN",
                            "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    
        if x is not None:
            return self.format_string(str(x))
        else:
            return ""
    
    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    
        lstr, rstr = (x.split('.') + [''])[:2]
        lstrrev = lstr[::-1]
        a = [''] * 5
    
        if len(lstrrev) % 3 == 1:
            lstrrev += "00"
        elif len(lstrrev) % 3 == 2:
            lstrrev += "0"
    
        lm = ""
        for i in range(len(lstrrev) // 3):
            a[i] = lstrrev[3 * i:3 * i + 3][::-1]
            if a[i] != "000":
                lm = self.trans_three(a[i]) + " " + self.parse_more(i) + " " + lm
            else:
                lm += self.trans_three(a[i])
    
        xs = f"AND CENTS {self.trans_two(rstr)} " if rstr else ""
        if not lm.strip():
            return "ZERO ONLY"
        else:
            return f"{lm.strip()} {xs}ONLY"
    
    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
    
        if s[0] == "0":
            return self.trans_two(s[1:])
        elif s[1:] == "00":
            return f"{self.NUMBER[int(s[0])]} HUNDRED"
        else:
            return f"{self.NUMBER[int(s[0])]} HUNDRED AND {self.trans_two(s[1:])}"
    
    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
    
        return self.NUMBER_MORE[i]
    
    def trans_two(self, s):
        """
        Converte un numero a due cifre nella sua rappresentazione in parole.
        :param s: str, il numero a due cifre
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        if s[0] == "1":
            return self.NUMBER_TEEN[int(s[1])] if s[1] != "0" else self.NUMBER_TEEN[0]
        elif s[0] == "0":
            return self.NUMBER[int(s[1])]
        else:
            return f"{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}"