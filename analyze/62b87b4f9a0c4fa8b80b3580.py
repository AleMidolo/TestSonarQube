def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    total = 0.0
    for i in range(len(bins)):
        # Calculate width of each bin
        bin_width = edges[i + 1] - edges[i]
        # Multiply bin height by width and add to total
        total += bins[i] * bin_width
    return total