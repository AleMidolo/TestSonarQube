def trans_three(self, s):
    """
    Converts a three-digit number into words format
    :param s: str, the three-digit number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_three("123")
    "ONE HUNDRED AND TWENTY THREE"
    """
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    # Pad with zeros if needed
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
            if result and s[1] == '0':
                result.append("AND")
            result.append(ones[int(s[2])])
    
    return " ".join(result)