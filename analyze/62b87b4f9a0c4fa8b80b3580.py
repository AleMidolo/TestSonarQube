def integral(bins, edges):
    """
    Calcular la integral (escala para un histograma).

    *bins* contiene los valores, y *edges* forman la malla  
    para la integración.  
    Su formato está definido en la descripción de la clase :class:`.histogram`.
    """
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges.")
    
    # Calculate the width of each bin
    widths = edges[1:] - edges[:-1]
    
    # Calculate the integral as the sum of the area of each bin
    integral_value = sum(bins * widths)
    
    return integral_value