def integral(bins, edges):
    """
    Calcular la integral (escala para un histograma).

    *bins* contiene los valores, y *edges* forman la malla  
    para la integración.  
    Su formato está definido en la descripción de la clase :class:`.histogram`.
    """
    total = 0.0
    for i in range(len(bins)):
        # Calculate width of each bin
        width = edges[i+1] - edges[i]
        # Multiply bin height by width and add to total
        total += bins[i] * width
    return total