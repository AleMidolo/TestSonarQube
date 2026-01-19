def trans_two(self, s):
    """
    将两位数转换为单词格式
    :param s: str, 两位数
    :return: str, 单词格式的数字
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "TWENTY THREE"
    """
    if not s or s == "00":
        return ""
    
    # Define mappings
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    # Handle single digit (0X format)
    if len(s) == 1 or s[0] == '0':
        digit = int(s[-1])
        return ones[digit]
    
    # Get the two digits
    ten_digit = int(s[0])
    one_digit = int(s[1])
    
    # Handle teens (10-19)
    if ten_digit == 1:
        return teens[one_digit]
    
    # Handle other two-digit numbers
    result = tens[ten_digit]
    if one_digit > 0:
        if result:
            result += " " + ones[one_digit]
        else:
            result = ones[one_digit]
    
    return result