def integral(bins, edges):
    """
    Calcular la integral (escala para un histograma).

    *bins* contiene los valores, y *edges* forman la malla  
    para la integración.  
    Su formato está definido en la descripción de la clase :class:`.histogram`.
    """
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges.")
    
    integral_value = 0.0
    for i in range(len(bins)):
        width = edges[i + 1] - edges[i]
        integral_value += bins[i] * width
    
    return integral_value