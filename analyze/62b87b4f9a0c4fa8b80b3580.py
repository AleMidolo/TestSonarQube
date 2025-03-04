def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    total = 0.0
    
    # Iterate through bins and edges to compute integral
    for i in range(len(bins)):
        # Width of current bin
        width = edges[i+1] - edges[i]
        # Area = height * width
        area = bins[i] * width
        total += area
        
    return total