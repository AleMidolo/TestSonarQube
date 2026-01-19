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
    
    # If the number is 0, return empty string (based on typical usage)
    if s == '0':
        return ""
    
    # Pad with leading zeros to make it 3 digits
    s = s.zfill(3)
    
    result = []
    
    # Hundreds place
    if s[0] != '0':
        result.append(ones[int(s[0])])
        result.append("HUNDRED")
    
    # Tens and ones place
    if s[1] == '1':  # Teens (10-19)
        if result:
            result.append("AND")
        result.append(teens[int(s[2])])
    else:
        if s[1] != '0':  # Tens place
            if result:
                result.append("AND")
            result.append(tens[int(s[1])])
        
        if s[2] != '0':  # Ones place
            if result and s[1] == '0':  # Only add AND if we have hundreds but no tens
                result.append("AND")
            result.append(ones[int(s[2])])
    
    return " ".join(result)