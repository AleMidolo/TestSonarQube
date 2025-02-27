def integral(bins, edges):
    """
    Calcola l'integrale (scala per un istogramma).

    *i bins* contengono i valori, mentre *gli edges* formano la griglia  
    per l'integrazione.  
    Il loro formato è definito nella descrizione della classe :class:`.histogram`.
    """
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges.")
    
    integral_value = 0.0
    for i in range(len(bins)):
        width = edges[i + 1] - edges[i]
        integral_value += bins[i] * width
    
    return integral_value