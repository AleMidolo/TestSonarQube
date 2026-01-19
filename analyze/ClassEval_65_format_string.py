def format_string(self, x):
    """
    Converts a string representation of a number into words format
    :param x: str, the string representation of a number
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    # Handle empty string or zero
    if not x or int(x) == 0:
        return "ZERO ONLY"
    
    # Remove leading zeros
    x = x.lstrip('0')
    if not x:
        return "ZERO ONLY"
    
    # Define word mappings
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    def convert_hundreds(num):
        """Convert a number less than 1000 to words"""
        result = []
        
        # Hundreds place
        hundreds_digit = num // 100
        if hundreds_digit > 0:
            result.append(ones[hundreds_digit])
            result.append("HUNDRED")
        
        # Tens and ones place
        remainder = num % 100
        if remainder > 0:
            if result:  # Add "AND" if we had hundreds
                result.append("AND")
            
            if remainder < 10:
                result.append(ones[remainder])
            elif remainder < 20:
                result.append(teens[remainder - 10])
            else:
                tens_digit = remainder // 10
                ones_digit = remainder % 10
                result.append(tens[tens_digit])
                if ones_digit > 0:
                    result.append(ones[ones_digit])
        
        return " ".join(result)
    
    # Convert string to integer
    num = int(x)
    
    # Break number into groups of thousands
    if num < 1000:
        words = convert_hundreds(num)
    elif num < 1000000:
        thousands = num // 1000
        remainder = num % 1000
        
        words = convert_hundreds(thousands) + " THOUSAND"
        if remainder > 0:
            words += " " + convert_hundreds(remainder)
    else:
        millions = num // 1000000
        remainder = num % 1000000
        
        words = convert_hundreds(millions) + " MILLION"
        
        if remainder >= 1000:
            thousands = remainder // 1000
            words += " " + convert_hundreds(thousands) + " THOUSAND"
            remainder = remainder % 1000
        
        if remainder > 0:
            words += " " + convert_hundreds(remainder)
    
    return words + " ONLY"