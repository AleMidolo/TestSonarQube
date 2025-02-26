def integral(bins, edges):
    """
    Calcola l'integrale (scala per un istogramma).

    *i bins* contengono i valori, mentre *gli edges* formano la griglia  
    per l'integrazione.  
    Il loro formato è definito nella descrizione della classe :class:`.histogram`.
    """
    return sum((edges[i + 1] - edges[i]) * bins[i] for i in range(len(bins)))