def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    integral_value = 0.0
    for i in range(len(bins)):
        bin_width = edges[i+1] - edges[i]
        integral_value += bins[i] * bin_width
    return integral_value