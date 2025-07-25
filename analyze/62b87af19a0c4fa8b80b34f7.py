def difference(d1, d2, level=-1):
    """
    Restituisce un dizionario con gli elementi di *d1* che non sono contenuti in *d2*.

    Il parametro *level* definisce la profondità massima della ricorsione. Per una ricorsione infinita, 
    impostare *level* a -1. Per livello 1, se una chiave è presente sia in *d1* che in *d2* ma ha valori diversi,
    viene inclusa nella differenza. Consulta la funzione :func:`intersection` per ulteriori dettagli.

    *d1* e *d2* rimangono invariati. Tuttavia, *d1* o alcuni dei suoi sottodizionari potrebbero essere 
    restituiti direttamente. Effettua una copia profonda (deep copy) del risultato quando appropriato.
    """
    result = {}
    
    # Per ogni chiave in d1
    for key in d1:
        # Se la chiave non è in d2, aggiungi l'intero valore al risultato
        if key not in d2:
            result[key] = d1[key]
        # Se siamo al livello massimo di ricorsione e i valori sono diversi
        elif level == 1 and d1[key] != d2[key]:
            result[key] = d1[key]
        # Se non siamo al livello massimo e entrambi i valori sono dizionari
        elif level != 1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            # Calcola ricorsivamente la differenza dei sottodizionari
            new_level = level - 1 if level > 0 else -1
            sub_diff = difference(d1[key], d2[key], new_level)
            if sub_diff:  # Se c'è una differenza, aggiungila al risultato
                result[key] = sub_diff
        # Se i valori sono diversi e non sono entrambi dizionari
        elif d1[key] != d2[key]:
            result[key] = d1[key]
            
    return result