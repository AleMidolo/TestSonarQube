def format(self, x):
    """
    Converts a number into words format
    :param x: int or float, the number to be converted into words format
    :return: str, the number in words format
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
    """
    if x == 0:
        return "ZERO ONLY"
    
    # Handle negative numbers
    if x < 0:
        return "MINUS " + self.format(-x)
    
    # Separate integer and decimal parts
    if isinstance(x, float):
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)
        result = self._convert_integer(integer_part)
        if decimal_part > 0:
            result += " AND " + self._convert_integer(decimal_part) + " CENTS"
        return result + " ONLY"
    else:
        return self._convert_integer(x) + " ONLY"

def _convert_integer(self, n):
    """Helper method to convert integer to words"""
    if n == 0:
        return ""
    
    ones = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", 
             "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    
    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        return (tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")).strip()
    elif n < 1000:
        hundred_part = ones[n // 100] + " HUNDRED"
        remainder = n % 100
        if remainder > 0:
            return hundred_part + " AND " + self._convert_integer(remainder)
        return hundred_part
    elif n < 1000000:
        thousand_part = self._convert_integer(n // 1000) + " THOUSAND"
        remainder = n % 1000
        if remainder > 0:
            return thousand_part + " " + self._convert_integer(remainder)
        return thousand_part
    elif n < 1000000000:
        million_part = self._convert_integer(n // 1000000) + " MILLION"
        remainder = n % 1000000
        if remainder > 0:
            return million_part + " " + self._convert_integer(remainder)
        return million_part
    else:
        billion_part = self._convert_integer(n // 1000000000) + " BILLION"
        remainder = n % 1000000000
        if remainder > 0:
            return billion_part + " " + self._convert_integer(remainder)
        return billion_part