import copy

def difference(d1, d2, level=-1):
    """
    Restituisce un dizionario con gli elementi di *d1* che non sono contenuti in *d2*.

    Il parametro *level* definisce la profondità massima della ricorsione. Per una ricorsione infinita, impostare *level* a -1. Per livello 1, se una chiave è presente sia in *d1* che in *d2* ma ha valori diversi, viene inclusa nella differenza. Consulta la funzione :func:`intersection` per ulteriori dettagli.

    *d1* e *d2* rimangono invariati. Tuttavia, *d1* o alcuni dei suoi sottodizionari potrebbero essere restituiti direttamente. Effettua una copia profonda (deep copy) del risultato quando appropriato.

    .. versione aggiunta:: 0.5
       Aggiunto il parametro *level*.
    """
    if level == 0:
        return {}
    
    diff = {}
    for key in d1:
        if key not in d2:
            diff[key] = copy.deepcopy(d1[key])
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if level != 1:
                sub_diff = difference(d1[key], d2[key], level - 1 if level != -1 else -1)
                if sub_diff:
                    diff[key] = sub_diff
        elif d1[key] != d2[key]:
            diff[key] = copy.deepcopy(d1[key])
    
    return diff