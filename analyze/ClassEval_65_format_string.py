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
    
    # Split number into groups of three from right
    num_int = int(x)
    
    if num_int < 1000:
        return convert_below_thousand(num_int) + " ONLY"
    elif num_int < 1000000:
        thousands = num_int // 1000
        remainder = num_int % 1000
        result = convert_below_thousand(thousands) + " THOUSAND"
        if remainder != 0:
            result += " " + convert_below_thousand(remainder)
        return result + " ONLY"
    elif num_int < 1000000000:
        millions = num_int // 1000000
        remainder = num_int % 1000000
        result = convert_below_thousand(millions) + " MILLION"
        if remainder >= 1000:
            thousands = remainder // 1000
            result += " " + convert_below_thousand(thousands) + " THOUSAND"
            remainder = remainder % 1000
        if remainder != 0:
            result += " " + convert_below_thousand(remainder)
        return result + " ONLY"
    else:
        billions = num_int // 1000000000
        remainder = num_int % 1000000000
        result = convert_below_thousand(billions) + " BILLION"
        if remainder >= 1000000:
            millions = remainder // 1000000
            result += " " + convert_below_thousand(millions) + " MILLION"
            remainder = remainder % 1000000
        if remainder >= 1000:
            thousands = remainder // 1000
            result += " " + convert_below_thousand(thousands) + " THOUSAND"
            remainder = remainder % 1000
        if remainder != 0:
            result += " " + convert_below_thousand(remainder)
        return result + " ONLY"