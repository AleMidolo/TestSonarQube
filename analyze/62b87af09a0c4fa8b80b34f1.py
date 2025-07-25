def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.
    
    Coordinates outside the histogram edges are ignored.
    """
    # Check if coord is within histogram bounds
    for i, x in enumerate(coord):
        if x < self.edges[i][0] or x >= self.edges[i][-1]:
            return
            
    # Find bin indices for each dimension
    indices = []
    for dim, x in enumerate(coord):
        # Find the bin index using binary search
        idx = np.searchsorted(self.edges[dim], x) - 1
        indices.append(idx)
        
    # Add weight to the bin
    self.hist[tuple(indices)] += weight