def trans_three(self, s):
    """
    将三位数转换为单词格式
    :param s: str，三位数
    :return: str，数字的单词格式
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_three("123")
    "ONE HUNDRED AND TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    # Remove leading zeros and pad to ensure we can process
    s = s.lstrip('0') or '0'
    
    if s == '0':
        return ""
    
    # Pad to 3 digits for easier processing
    s = s.zfill(3)
    
    result = []
    
    # Hundreds place
    if s[0] != '0':
        result.append(ones[int(s[0])])
        result.append("HUNDRED")
    
    # Tens and ones place
    tens_ones = int(s[1:])
    
    if tens_ones > 0:
        if result:  # If we have hundreds, add "AND"
            result.append("AND")
        
        if 10 <= tens_ones <= 19:
            result.append(teens[tens_ones - 10])
        else:
            if s[1] != '0':
                result.append(tens[int(s[1])])
            if s[2] != '0':
                result.append(ones[int(s[2])])
    
    return " ".join(result)