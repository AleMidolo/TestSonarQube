def format(self, x):
    """
    Converts a number into words format
    :param x: int or float, the number to be converted into words format
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    if x == 0:
        return "ZERO ONLY"
    
    # Handle negative numbers
    if x < 0:
        return "MINUS " + self.format(-x)
    
    # Separate integer and decimal parts
    if isinstance(x, float):
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)
        if decimal_part > 0:
            result = self.format(integer_part).replace(" ONLY", "")
            result += " AND " + self.format(decimal_part).replace(" ONLY", "") + " CENTS ONLY"
            return result
        else:
            x = integer_part
    
    # Define word mappings
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            result = tens[n // 10]
            if n % 10 != 0:
                result += " " + ones[n % 10]
            return result
        else:
            result = ones[n // 100] + " HUNDRED"
            remainder = n % 100
            if remainder != 0:
                result += " AND " + convert_below_thousand(remainder)
            return result
    
    # Handle numbers by groups of thousands
    if x < 1000:
        return convert_below_thousand(x) + " ONLY"
    elif x < 1000000:
        thousands = x // 1000
        remainder = x % 1000
        result = convert_below_thousand(thousands) + " THOUSAND"
        if remainder != 0:
            result += " " + convert_below_thousand(remainder)
        return result + " ONLY"
    elif x < 1000000000:
        millions = x // 1000000
        remainder = x % 1000000
        result = convert_below_thousand(millions) + " MILLION"
        if remainder >= 1000:
            thousands = remainder // 1000
            result += " " + convert_below_thousand(thousands) + " THOUSAND"
            remainder = remainder % 1000
        if remainder != 0:
            result += " " + convert_below_thousand(remainder)
        return result + " ONLY"
    else:
        billions = x // 1000000000
        remainder = x % 1000000000
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