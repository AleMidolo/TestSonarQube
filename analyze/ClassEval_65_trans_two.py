def trans_two(self, s):
    """
    Converts a two-digit number into words format
    :param s: str, the two-digit number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if not s or s == "00":
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