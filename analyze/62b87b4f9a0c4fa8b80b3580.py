def integral(bins, edges):
    """
    Calcola l'integrale (scala per un istogramma).

    *i bins* contengono i valori, mentre *gli edges* formano la griglia  
    per l'integrazione.  
    Il loro formato è definito nella descrizione della classe :class:`.histogram`.
    """
    integral_value = 0.0
    for i in range(len(bins)):
        bin_width = edges[i+1] - edges[i]
        integral_value += bins[i] * bin_width
    return integral_value