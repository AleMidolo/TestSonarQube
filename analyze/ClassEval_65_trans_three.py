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
    teens = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", 
             "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    tens = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", 
            "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    # Rimuovi zeri iniziali e converti in intero
    num = int(s)
    
    if num == 0:
        return "ZERO"
    
    result = []
    
    # Centinaia
    hundreds = num // 100
    if hundreds > 0:
        if hundreds == 1:
            result.append("UNO CENTO")
        else:
            result.append(ones[hundreds] + " CENTO")
    
    # Decine e unità
    remainder = num % 100
    
    if remainder >= 10 and remainder < 20:
        # Numeri da 10 a 19
        if result:
            result.append("E")
        result.append(teens[remainder - 10])
    else:
        # Decine
        tens_digit = remainder // 10
        ones_digit = remainder % 10
        
        if tens_digit > 0:
            if result:
                result.append("E")
            result.append(tens[tens_digit])
        
        # Unità
        if ones_digit > 0:
            if tens_digit == 0 and result:
                result.append("E")
            result.append(ones[ones_digit])
    
    return " ".join(result)