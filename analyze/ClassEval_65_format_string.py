def format_string(self, x):
    """
    Converts a string representation of a number into words format
    :param x: str, the string representation of a number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    # Handle edge cases
    if not x or x == "0":
        return "ZERO ONLY"
    
    # Remove leading zeros
    x = x.lstrip("0")
    if not x:
        return "ZERO ONLY"
    
    # Define word mappings
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_below_thousand(num):
        """Convert a number below 1000 to words"""
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            result = tens[num // 10]
            if num % 10 != 0:
                result += " " + ones[num % 10]
            return result
        else:
            result = ones[num // 100] + " HUNDRED"
            remainder = num % 100
            if remainder != 0:
                result += " AND " + convert_below_thousand(remainder)
            return result
    
    # Split number into groups of three from right to left
    num_int = int(x)
    
    if num_int < 1000:
        return convert_below_thousand(num_int) + " ONLY"
    
    # Handle thousands, millions, billions
    scale = ["", "THOUSAND", "MILLION", "BILLION"]
    groups = []
    
    temp = num_int
    while temp > 0:
        groups.append(temp % 1000)
        temp //= 1000
    
    result_parts = []
    for i in range(len(groups) - 1, -1, -1):
        if groups[i] != 0:
            part = convert_below_thousand(groups[i])
            if i > 0:
                part += " " + scale[i]
            result_parts.append(part)
    
    return " ".join(result_parts) + " ONLY"