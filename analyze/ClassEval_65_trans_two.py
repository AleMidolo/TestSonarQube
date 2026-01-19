def trans_two(self, s):
    """
    दो अंकों की संख्या को शब्दों के प्रारूप में परिवर्तित करता है
    :param s: str, दो अंकों की संख्या
    :return: str, संख्या शब्दों के प्रारूप में
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if len(s) == 0 or int(s) == 0:
        return ""
    
    num = int(s)
    
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + " " + ones[ones_digit]