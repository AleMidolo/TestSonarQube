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
        result = self._convert_integer(int_part)
        if decimal_part > 0:
            result += " VIRGOLA " + self._convert_integer(decimal_part)
        return result
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
                result = "CENTO"
            else:
                result = ones[hundred] + "CENTO"
            if rest > 0:
                result += " " + convert_below_thousand(rest)
            return result
    
    if n < 1000:
        return convert_below_thousand(n)
    elif n < 1000000:
        thousands = n // 1000
        rest = n % 1000
        if thousands == 1:
            result = "MILLE"
        else:
            result = convert_below_thousand(thousands) + " MILA"
        if rest > 0:
            result += " " + convert_below_thousand(rest)
        return result
    else:
        millions = n // 1000000
        rest = n % 1000000
        if millions == 1:
            result = "UN MILIONE"
        else:
            result = convert_below_thousand(millions) + " MILIONI"
        if rest > 0:
            result += " " + self._convert_integer(rest)
        return result