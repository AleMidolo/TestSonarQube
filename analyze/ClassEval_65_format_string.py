def format_string(self, x):
    """
    Converte una rappresentazione stringa di un numero nella sua rappresentazione in parole.
    :param x: str, la rappresentazione stringa di un numero
    :return: str, il numero nel formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "UNO CENTO E VENTITRE MILA QUATTROCENTO E CINQUANTA SEI SOLO"
    """
    if not x or not x.isdigit():
        return ""
    
    # Rimuovi zeri iniziali
    x = x.lstrip('0') or '0'
    
    # Definizioni base
    unita = ['', 'UNO', 'DUE', 'TRE', 'QUATTRO', 'CINQUE', 'SEI', 'SETTE', 'OTTO', 'NOVE']
    decine_speciali = ['DIECI', 'UNDICI', 'DODICI', 'TREDICI', 'QUATTORDICI', 'QUINDICI', 
                       'SEDICI', 'DICIASSETTE', 'DICIOTTO', 'DICIANNOVE']
    decine = ['', '', 'VENTI', 'TRENTA', 'QUARANTA', 'CINQUANTA', 'SESSANTA', 'SETTANTA', 'OTTANTA', 'NOVANTA']
    
    def converti_centinaia(num):
        """Converte un numero da 0 a 999 in parole"""
        if num == 0:
            return ''
        
        risultato = []
        
        # Centinaia
        centinaia = num // 100
        if centinaia > 0:
            risultato.append(unita[centinaia])
            risultato.append('CENTO')
        
        # Decine e unità
        resto = num % 100
        if resto >= 10 and resto < 20:
            if risultato:
                risultato.append('E')
            risultato.append(decine_speciali[resto - 10])
        else:
            dec = resto // 10
            uni = resto % 10
            
            if dec > 0:
                if risultato:
                    risultato.append('E')
                risultato.append(decine[dec])
            
            if uni > 0:
                risultato.append(unita[uni])
        
        return ' '.join(risultato)
    
    # Dividi il numero in gruppi di tre cifre da destra
    num_int = int(x)
    
    if num_int == 0:
        return "ZERO SOLO"
    
    # Gestisci migliaia e unità
    migliaia = num_int // 1000
    unita_parte = num_int % 1000
    
    risultato = []
    
    if migliaia > 0:
        risultato.append(converti_centinaia(migliaia))
        risultato.append('MILA')
    
    if unita_parte > 0:
        risultato.append(converti_centinaia(unita_parte))
    
    risultato.append('SOLO')
    
    return ' '.join(risultato)