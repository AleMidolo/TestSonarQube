def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    total = 0.0
    
    # Iterate through bins and calculate area for each bin
    for i in range(len(bins)):
        # Width of the bin is difference between edges
        bin_width = edges[i + 1] - edges[i]
        # Area is bin height * width
        bin_area = bins[i] * bin_width
        total += bin_area
        
    return total