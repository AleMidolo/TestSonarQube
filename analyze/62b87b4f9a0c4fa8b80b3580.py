def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges.")
    
    integral_value = 0.0
    for i in range(len(bins)):
        width = edges[i + 1] - edges[i]
        integral_value += bins[i] * width
    
    return integral_value