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
    
    def convert_hundreds(num):
        """Convert a number less than 1000 to words"""
        result = []
        
        # Hundreds place
        hundred = num // 100
        if hundred > 0:
            result.append(ones[hundred])
            result.append("HUNDRED")
        
        # Tens and ones place
        remainder = num % 100
        if remainder > 0:
            if result:  # If we had hundreds, add "AND"
                result.append("AND")
            
            if 10 <= remainder < 20:
                result.append(teens[remainder - 10])
            else:
                ten = remainder // 10
                one = remainder % 10
                if ten > 0:
                    result.append(tens[ten])
                if one > 0:
                    result.append(ones[one])
        
        return " ".join(result)
    
    # Convert string to integer
    num = int(x)
    
    if num == 0:
        return "ZERO ONLY"
    
    result = []
    
    # Billions
    if num >= 1000000000:
        billions = num // 1000000000
        result.append(convert_hundreds(billions))
        result.append("BILLION")
        num %= 1000000000
    
    # Millions
    if num >= 1000000:
        millions = num // 1000000
        result.append(convert_hundreds(millions))
        result.append("MILLION")
        num %= 1000000
    
    # Thousands
    if num >= 1000:
        thousands = num // 1000
        result.append(convert_hundreds(thousands))
        result.append("THOUSAND")
        num %= 1000
    
    # Remaining hundreds, tens, ones
    if num > 0:
        result.append(convert_hundreds(num))
    
    return " ".join(result) + " ONLY"