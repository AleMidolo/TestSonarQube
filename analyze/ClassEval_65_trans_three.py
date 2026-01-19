def trans_three(self, s):
    """
    Converte un numero di tre cifre nella sua rappresentazione in parole.
    :param s: str, il numero di tre cifre
    :return: str, il numero in formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_three("123")
    "UNO CENTO E VENTI TRE"
    """
    # Definizione dei numeri in italiano
    ones = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    
    # Padding per assicurarsi che sia di 3 cifre
    s = s.zfill(3)
    
    result = []
    
    # Centinaia
    hundreds_digit = int(s[0])
    if hundreds_digit > 0:
        if hundreds_digit == 1:
            result.append("UNO CENTO")
        else:
            result.append(ones[hundreds_digit] + " CENTO")
    
    # Decine e unità
    tens_digit = int(s[1])
    ones_digit = int(s[2])
    
    if tens_digit == 1:
        # Numeri da 10 a 19
        result.append(teens[ones_digit])
    else:
        # Decine
        if tens_digit > 0:
            result.append(tens[tens_digit])
        # Unità
        if ones_digit > 0:
            result.append(ones[ones_digit])
    
    return " E ".join(result) if result else ""