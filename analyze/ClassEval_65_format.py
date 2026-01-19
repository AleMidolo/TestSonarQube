def format(self, x):
    """
    将数字转换为单词格式
    :param x: int 或 float，要转换为单词格式的数字
    :return: str，数字的单词格式
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
        decimal_part = str(x).split('.')[1]
        result = self.format(integer_part).replace(" ONLY", "")
        result += " POINT"
        for digit in decimal_part:
            result += " " + self._convert_ones(int(digit))
        return result + " ONLY"
    
    x = int(x)
    
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
    
    # Process number in groups of thousands
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

def _convert_ones(self, n):
    ones = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    return ones[n]