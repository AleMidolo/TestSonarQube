def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    total = 0.0
    
    # Ensure bins and edges have compatible lengths
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be equal to length of edges minus 1")
        
    # Iterate through bins and calculate area for each bin
    for i in range(len(bins)):
        # Width of the bin
        width = edges[i+1] - edges[i]
        # Area = height * width
        area = bins[i] * width
        total += area
        
    return total