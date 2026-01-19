def format(self, x):
    """
    एक संख्या को शब्दों के प्रारूप में परिवर्तित करता है
    :param x: int या float, वह संख्या जिसे शब्दों के प्रारूप में परिवर्तित किया जाना है
    :return: str, संख्या शब्दों के प्रारूप में
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    if x == 0:
        return "ZERO ONLY"
    
    # Handle negative numbers
    if x < 0:
        return "MINUS " + self.format(-x)
    
    # Handle decimal numbers
    if isinstance(x, float) and x != int(x):
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)
        result = self.format(integer_part).replace(" ONLY", "")
        if decimal_part > 0:
            return result + " AND " + self.format(decimal_part).replace(" ONLY", "") + " PAISE ONLY"
        return result + " ONLY"
    
    x = int(x)
    
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
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            hundred_part = ones[n // 100] + " HUNDRED"
            remainder = n % 100
            if remainder > 0:
                return hundred_part + " AND " + convert_below_thousand(remainder)
            return hundred_part
    
    if x < 1000:
        return convert_below_thousand(x) + " ONLY"
    
    # Handle thousands and above
    parts = []
    
    # Millions
    if x >= 1000000:
        millions = x // 1000000
        parts.append(convert_below_thousand(millions) + " MILLION")
        x %= 1000000
    
    # Thousands
    if x >= 1000:
        thousands = x // 1000
        parts.append(convert_below_thousand(thousands) + " THOUSAND")
        x %= 1000
    
    # Remaining hundreds
    if x > 0:
        parts.append(convert_below_thousand(x))
    
    result = " ".join(parts) + " ONLY"
    return result