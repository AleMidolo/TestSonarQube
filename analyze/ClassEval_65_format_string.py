def format_string(self, x):
    """
    Converts a string representation of a number into words format
    :param x: str, the string representation of a number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    # Define word mappings
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_below_thousand(n):
        """Convert numbers below 1000 to words"""
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
    
    # Handle zero case
    num = int(x)
    if num == 0:
        return "ZERO ONLY"
    
    # Process the number in groups of thousands
    result_parts = []
    
    # Billions
    if num >= 1000000000:
        billions = num // 1000000000
        result_parts.append(convert_below_thousand(billions) + " BILLION")
        num %= 1000000000
    
    # Millions
    if num >= 1000000:
        millions = num // 1000000
        result_parts.append(convert_below_thousand(millions) + " MILLION")
        num %= 1000000
    
    # Thousands
    if num >= 1000:
        thousands = num // 1000
        result_parts.append(convert_below_thousand(thousands) + " THOUSAND")
        num %= 1000
    
    # Hundreds, tens, ones
    if num > 0:
        result_parts.append(convert_below_thousand(num))
    
    result = " ".join(result_parts)
    return result + " ONLY"