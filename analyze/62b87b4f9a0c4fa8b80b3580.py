def integral(bins, edges):
    """
    Calcular la integral (escala para un histograma).

    *bins* contiene los valores, y *edges* forman la malla  
    para la integración.  
    Su formato está definido en la descripción de la clase :class:`.histogram`.
    """
    total = 0.0
    for i in range(len(bins)):
        bin_width = edges[i+1] - edges[i]
        total += bins[i] * bin_width
    return total