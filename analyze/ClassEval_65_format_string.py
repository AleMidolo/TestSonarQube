def format_string(self, x):
    """
    Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
    :param x: str, la rappresentazione stringa di un numero
    :return: str, il numero nel formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "UNO CENTO E VENTITRE MILA QUATTROCENTO E CINQUANTA SEI SOLO"
    """
    # Definizione delle parole per i numeri
    unita = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
    decine_speciali = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", 
                       "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
    decine = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]
    
    def converti_centinaia(num):
        """Converte un numero di massimo 3 cifre in parole"""
        if num == 0:
            return ""
        
        risultato = []
        
        # Centinaia
        centinaia = num // 100
        if centinaia > 0:
            risultato.append(unita[centinaia])
            risultato.append("CENTO")
        
        # Decine e unità
        resto = num % 100
        if 10 <= resto <= 19:
            if risultato:
                risultato.append("E")
            risultato.append(decine_speciali[resto - 10])
        else:
            dec = resto // 10
            uni = resto % 10
            
            if dec > 0:
                if risultato:
                    risultato.append("E")
                risultato.append(decine[dec])
            
            if uni > 0:
                risultato.append(unita[uni])
        
        return " ".join(risultato)
    
    # Rimuovi spazi e converti in intero
    x = x.strip()
    numero = int(x)
    
    if numero == 0:
        return "ZERO SOLO"
    
    # Dividi in migliaia e resto
    migliaia = numero // 1000
    resto = numero % 1000
    
    risultato = []
    
    if migliaia > 0:
        risultato.append(converti_centinaia(migliaia))
        risultato.append("MILA")
    
    if resto > 0:
        risultato.append(converti_centinaia(resto))
    
    risultato.append("SOLO")
    
    return " ".join(risultato)