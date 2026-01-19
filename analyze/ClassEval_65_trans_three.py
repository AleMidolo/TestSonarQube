def trans_three(self, s):
    """
    Converte un numero di tre cifre nella sua rappresentazione in parole.
    :param s: str, il numero di tre cifre
    :return: str, il numero in formato parole
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_three("123")
    "UNO CENTO E VENTI TRE"
    """
    # Dizionari per la conversione
    ones = {
        '0': '', '1': 'UNO', '2': 'DUE', '3': 'TRE', '4': 'QUATTRO',
        '5': 'CINQUE', '6': 'SEI', '7': 'SETTE', '8': 'OTTO', '9': 'NOVE'
    }
    
    tens = {
        '2': 'VENTI', '3': 'TRENTA', '4': 'QUARANTA', '5': 'CINQUANTA',
        '6': 'SESSANTA', '7': 'SETTANTA', '8': 'OTTANTA', '9': 'NOVANTA'
    }
    
    teens = {
        '10': 'DIECI', '11': 'UNDICI', '12': 'DODICI', '13': 'TREDICI',
        '14': 'QUATTORDICI', '15': 'QUINDICI', '16': 'SEDICI',
        '17': 'DICIASSETTE', '18': 'DICIOTTO', '19': 'DICIANNOVE'
    }
    
    # Padding per assicurarsi che sia di 3 cifre
    s = s.zfill(3)
    
    result = []
    
    # Centinaia
    if s[0] != '0':
        result.append(ones[s[0]])
        result.append('CENTO')
    
    # Decine e unità
    if s[1] == '1':  # Numeri da 10 a 19
        result.append('E')
        result.append(teens[s[1:3]])
    elif s[1] != '0':  # Decine da 20 a 90
        result.append('E')
        result.append(tens[s[1]])
        if s[2] != '0':
            result.append(ones[s[2]])
    elif s[2] != '0':  # Solo unità
        result.append('E')
        result.append(ones[s[2]])
    
    return ' '.join(result)