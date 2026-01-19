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
        result = self._convert_integer(int_part) + " VIRGOLA " + self._convert_integer(decimal_part)
        return result.strip()
    else:
        return (self._convert_integer(x) + " SOLO").strip()
    
def _convert_integer(self, n):
    if n == 0:
        return "ZERO"
    
    units = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    if n < 10:
        return units[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        ten = n // 10
        unit = n % 10
        if unit == 1 or unit == 8:
            return tens[ten][:-1] + units[unit]
        else:
            return (tens[ten] + units[unit]).strip()
    elif n < 1000:
        hundred = n // 100
        remainder = n % 100
        if hundred == 1:
            result = "CENTO"
        else:
            result = units[hundred] + "CENTO"
        if remainder > 0:
            result += " " + self._convert_integer(remainder)
        return result.strip()
    elif n < 1000000:
        thousand = n // 1000
        remainder = n % 1000
        if thousand == 1:
            result = "MILLE"
        else:
            result = self._convert_integer(thousand) + " MILA"
        if remainder > 0:
            result += " " + self._convert_integer(remainder)
        return result.strip()
    elif n < 1000000000:
        million = n // 1000000
        remainder = n % 1000000
        if million == 1:
            result = "UN MILIONE"
        else:
            result = self._convert_integer(million) + " MILIONI"
        if remainder > 0:
            result += " " + self._convert_integer(remainder)
        return result.strip()
    else:
        return str(n)