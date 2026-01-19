def trans_two(self, s):
    """
    将两位数转换为单词格式
    :param s: str, 两位数
    :return: str, 单词格式的数字
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if not s or s == "00":
        return ""
    
    num = int(s)
    
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    else:
        ten_digit = num // 10
        one_digit = num % 10
        if one_digit == 0:
            return tens[ten_digit]
        else:
            return tens[ten_digit] + " " + ones[one_digit]