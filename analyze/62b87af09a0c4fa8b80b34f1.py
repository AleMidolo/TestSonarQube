def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.
    
    Coordinates outside the histogram edges are ignored.
    """
    # Check if coord is within histogram bounds
    if not isinstance(coord, (list, tuple)):
        coord = [coord]
        
    # Check each dimension is within bounds
    for i, x in enumerate(coord):
        if x < self.edges[i][0] or x >= self.edges[i][-1]:
            return
            
    # Find bin indices for each dimension
    indices = []
    for dim, x in enumerate(coord):
        # Find the bin index using binary search
        edges = self.edges[dim]
        idx = 0
        for j in range(len(edges)-1):
            if edges[j] <= x < edges[j+1]:
                idx = j
                break
        indices.append(idx)
        
    # Add weight to the bin
    self.values[tuple(indices)] += weight