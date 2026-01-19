def format(self, x):
    """
    Converte un numero nella sua rappresentazione in parole.
    :param x: int o float, il numero da convertire in formato parole
    :return: str, il numero in formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "CENTO VENTITRE MILA QUATTROCENTO CINQUANTA SEI SOLO"
    """
    if isinstance(x, float):
        int_part = int(x)
        decimal_part = round((x - int_part) * 100)
        if decimal_part == 0:
            return self.format(int_part) + " SOLO"
        else:
            return self.format(int_part) + " VIRGOLA " + self.format(decimal_part)
    
    if x == 0:
        return "ZERO"
    
    units = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    def convert_below_thousand(n):
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
                result = "CENTO"
            else:
                result = units[hundred] + "CENTO"
            
            if remainder > 0:
                result += " " + convert_below_thousand(remainder)
            
            return result
    
    if x < 1000:
        return convert_below_thousand(x) + " SOLO"
    elif x < 1000000:
        thousands = x // 1000
        remainder = x % 1000
        
        if thousands == 1:
            result = "MILLE"
        else:
            result = convert_below_thousand(thousands) + " MILA"
        
        if remainder > 0:
            result += " " + convert_below_thousand(remainder)
        
        return result + " SOLO"
    else:
        millions = x // 1000000
        remainder = x % 1000000
        
        if millions == 1:
            result = "UN MILIONE"
        else:
            result = convert_below_thousand(millions) + " MILIONI"
        
        if remainder >= 1000:
            thousands = remainder // 1000
            if thousands == 1:
                result += " MILLE"
            else:
                result += " " + convert_below_thousand(thousands) + " MILA"
            remainder = remainder % 1000
        
        if remainder > 0:
            result += " " + convert_below_thousand(remainder)
        
        return result + " SOLO"