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
    widths = edges[1:] - edges[:-1]
    
    # Compute the integral as the sum of the area of each bin
    return sum(bins * widths)