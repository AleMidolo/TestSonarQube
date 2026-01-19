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
            return self._convert_integer(int_part) + " SOLO"
        else:
            return self._convert_integer(int_part) + " VIRGOLA " + self._convert_integer(decimal_part)
    else:
        return self._convert_integer(x) + " SOLO"
    
def _convert_integer(self, n):
    if n == 0:
        return "ZERO"
    
    ones = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    def convert_below_thousand(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            ten = num // 10
            one = num % 10
            if one in [1, 8]:
                return tens[ten][:-1] + ones[one]
            else:
                return tens[ten] + ones[one]
        else:
            hundred = num // 100
            rest = num % 100
            if hundred == 1:
                hundred_str = "CENTO"
            else:
                hundred_str = ones[hundred] + "CENTO"
            
            if rest == 0:
                return hundred_str
            else:
                return hundred_str + " " + convert_below_thousand(rest)
    
    if n < 1000:
        return convert_below_thousand(n)
    elif n < 1000000:
        thousands = n // 1000
        rest = n % 1000
        
        if thousands == 1:
            thousands_str = "MILLE"
        else:
            thousands_str = convert_below_thousand(thousands) + " MILA"
        
        if rest == 0:
            return thousands_str
        else:
            return thousands_str + " " + convert_below_thousand(rest)
    else:
        millions = n // 1000000
        rest = n % 1000000
        
        if millions == 1:
            millions_str = "UN MILIONE"
        else:
            millions_str = convert_below_thousand(millions) + " MILIONI"
        
        if rest == 0:
            return millions_str
        elif rest < 1000:
            return millions_str + " " + convert_below_thousand(rest)
        else:
            return millions_str + " " + self._convert_integer(rest)