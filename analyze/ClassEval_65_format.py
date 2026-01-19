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
            if unit in [1, 8]:
                return tens[ten][:-1] + units[unit]
            else:
                return tens[ten] + units[unit]
        else:
            hundred = n // 100
            remainder = n % 100
            if hundred == 1:
                hundred_word = "CENTO"
            else:
                hundred_word = units[hundred] + "CENTO"
            
            if remainder > 0:
                return hundred_word + " " + convert_hundreds(remainder)
            else:
                return hundred_word
    
    def convert_number(num):
        if num == 0:
            return ""
        
        result = []
        
        # Billions
        if num >= 1000000000:
            billions = num // 1000000000
            if billions == 1:
                result.append("UN MILIARDO")
            else:
                result.append(convert_hundreds(billions) + " MILIARDI")
            num %= 1000000000
        
        # Millions
        if num >= 1000000:
            millions = num // 1000000
            if millions == 1:
                result.append("UN MILIONE")
            else:
                result.append(convert_hundreds(millions) + " MILIONI")
            num %= 1000000
        
        # Thousands
        if num >= 1000:
            thousands = num // 1000
            if thousands == 1:
                result.append("MILLE")
            else:
                result.append(convert_hundreds(thousands) + " MILA")
            num %= 1000
        
        # Hundreds, tens, units
        if num > 0:
            result.append(convert_hundreds(num))
        
        return " ".join(result)
    
    result = ""
    if is_negative:
        result = "MENO "
    
    result += convert_number(integer_part)
    
    if decimal_part:
        result += " VIRGOLA " + " ".join([units[int(d)] for d in decimal_part])
    else:
        result += " SOLO"
    
    return result.strip()