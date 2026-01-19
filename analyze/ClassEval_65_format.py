def format(self, x):
    """
    Converte un numero nella sua rappresentazione in parole.
    :param x: int o float, il numero da convertire in formato parole
    :return: str, il numero in formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "CENTO VENTITRE MILA QUATTROCENTO CINQUANTA SEI SOLO"
    """
    if x == 0:
        return "ZERO SOLO"
    
    # Separate integer and decimal parts
    if isinstance(x, float):
        parts = str(x).split('.')
        integer_part = int(parts[0])
        decimal_part = parts[1] if len(parts) > 1 else None
    else:
        integer_part = abs(int(x))
        decimal_part = None
    
    # Handle negative numbers
    is_negative = x < 0
    
    # Units, tens, and special numbers
    units = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    def convert_hundreds(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            ten = n // 10
            unit = n % 10
            result = tens[ten]
            if unit > 0:
                # Handle vowel elision
                if unit == 1 or unit == 8:
                    result = result[:-1] + units[unit]
                else:
                    result = result + units[unit]
            return result
        else:
            hundred = n // 100
            remainder = n % 100
            if hundred == 1:
                result = "CENTO"
            else:
                result = units[hundred] + "CENTO"
            if remainder > 0:
                result += " " + convert_hundreds(remainder)
            return result
    
    def convert_integer(n):
        if n == 0:
            return ""
        
        # Split into groups of thousands
        if n < 1000:
            return convert_hundreds(n)
        elif n < 1000000:
            thousands = n // 1000
            remainder = n % 1000
            if thousands == 1:
                result = "MILLE"
            else:
                result = convert_hundreds(thousands) + " MILA"
            if remainder > 0:
                result += " " + convert_hundreds(remainder)
            return result
        else:
            millions = n // 1000000
            remainder = n % 1000000
            if millions == 1:
                result = "UN MILIONE"
            else:
                result = convert_hundreds(millions) + " MILIONI"
            if remainder > 0:
                result += " " + convert_integer(remainder)
            return result
    
    result = ""
    if is_negative:
        result = "MENO "
    
    result += convert_integer(integer_part)
    
    if decimal_part:
        result += " VIRGOLA"
        for digit in decimal_part:
            result += " " + units[int(digit)]
    else:
        result += " SOLO"
    
    return result.strip()