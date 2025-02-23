def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges.")
    
    # Calculate the width of each bin
    widths = [edges[i + 1] - edges[i] for i in range(len(edges) - 1)]
    
    # Compute the integral as the sum of the area of each bin
    integral_value = sum(b * w for b, w in zip(bins, widths))
    
    return integral_value