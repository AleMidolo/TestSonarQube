def format_string(self, x):
    """
    Converts a string representation of a number into words format
    :param x: str, the string representation of a number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_below_thousand(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            hundred_part = ones[num // 100] + " HUNDRED"
            remainder = num % 100
            if remainder == 0:
                return hundred_part
            else:
                return hundred_part + " AND " + convert_below_thousand(remainder)
    
    # Remove leading zeros and handle empty string
    x = x.lstrip('0') or '0'
    num = int(x)
    
    if num == 0:
        return "ZERO ONLY"
    
    # Split number into groups of thousands
    billion = num // 1000000000
    million = (num % 1000000000) // 1000000
    thousand = (num % 1000000) // 1000
    remainder = num % 1000
    
    result = []
    
    if billion > 0:
        result.append(convert_below_thousand(billion) + " BILLION")
    
    if million > 0:
        result.append(convert_below_thousand(million) + " MILLION")
    
    if thousand > 0:
        result.append(convert_below_thousand(thousand) + " THOUSAND")
    
    if remainder > 0:
        result.append(convert_below_thousand(remainder))
    
    return " ".join(result) + " ONLY"