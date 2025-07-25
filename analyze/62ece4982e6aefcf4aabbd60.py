def size_to_bytes(size: str) -> int:
    units = {
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }
    
    # Se è solo un numero senza unità, restituisci il valore intero
    if size.isdigit():
        return int(size)
        
    # Estrai il numero e l'unità dalla stringa
    number = float(size[:-1])
    unit = size[-1].upper()
    
    # Moltiplica il numero per il fattore di conversione dell'unità
    if unit in units:
        return int(number * units[unit])
    else:
        raise ValueError(f"Unità non valida: {unit}")