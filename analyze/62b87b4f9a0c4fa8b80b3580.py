def integral(bins, edges):
    import numpy as np
    
    # Calculate the width of each bin
    bin_widths = np.diff(edges)
    
    # Calculate the area using the trapezoidal rule
    area = np.sum(bins * bin_widths)
    
    return area