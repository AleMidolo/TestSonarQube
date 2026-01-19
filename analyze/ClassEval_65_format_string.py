def format_string(self, x):
    """
    将数字的字符串表示转换为单词格式
    :param x: str，数字的字符串表示
    :return: str，数字的单词格式
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_below_thousand(num):
        """Convert numbers below 1000 to words"""
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
        else:  # num < 1000
            result = ones[num // 100] + " HUNDRED"
            remainder = num % 100
            if remainder != 0:
                result += " AND " + convert_below_thousand(remainder)
            return result
    
    # Convert string to integer
    num = int(x)
    
    if num == 0:
        return "ZERO ONLY"
    
    # Handle millions, thousands, and remainder
    millions = num // 1000000
    thousands = (num % 1000000) // 1000
    remainder = num % 1000
    
    result = []
    
    if millions > 0:
        result.append(convert_below_thousand(millions) + " MILLION")
    
    if thousands > 0:
        result.append(convert_below_thousand(thousands) + " THOUSAND")
    
    if remainder > 0:
        result.append(convert_below_thousand(remainder))
    
    return " ".join(result) + " ONLY"