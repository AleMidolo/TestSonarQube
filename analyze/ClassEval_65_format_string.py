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
    
    # Definizioni per la conversione
    unita = ['', 'UNO', 'DUE', 'TRE', 'QUATTRO', 'CINQUE', 'SEI', 'SETTE', 'OTTO', 'NOVE']
    decine_speciali = ['DIECI', 'UNDICI', 'DODICI', 'TREDICI', 'QUATTORDICI', 'QUINDICI', 
                       'SEDICI', 'DICIASSETTE', 'DICIOTTO', 'DICIANNOVE']
    decine = ['', '', 'VENTI', 'TRENTA', 'QUARANTA', 'CINQUANTA', 'SESSANTA', 'SETTANTA', 'OTTANTA', 'NOVANTA']
    
    def converti_centinaia(num_str):
        """Converte un numero di massimo 3 cifre in parole"""
        num = int(num_str)
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
    
    # Dividi il numero in gruppi di 3 cifre da destra
    lunghezza = len(x)
    
    if lunghezza <= 3:
        risultato = converti_centinaia(x)
    elif lunghezza <= 6:
        # Migliaia
        migliaia = x[:-3]
        centinaia = x[-3:]
        
        parti = []
        parte_migliaia = converti_centinaia(migliaia)
        if parte_migliaia:
            parti.append(parte_migliaia)
            parti.append('MILA')
        
        parte_centinaia = converti_centinaia(centinaia)
        if parte_centinaia:
            parti.append(parte_centinaia)
        
        risultato = ' '.join(parti)
    else:
        # Per numeri più grandi
        risultato = converti_centinaia(x[-3:])
    
    return risultato + ' SOLO' if risultato else 'SOLO'