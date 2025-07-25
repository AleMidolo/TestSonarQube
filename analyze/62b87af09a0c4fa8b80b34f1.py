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
            
    # Find the bin indices for each dimension
    indices = []
    for dim, x in enumerate(coord):
        # Find the bin index using binary search
        edges = self.edges[dim]
        left = 0
        right = len(edges) - 1
        
        while left < right:
            mid = (left + right) // 2
            if x < edges[mid]:
                right = mid
            else:
                left = mid + 1
                
        indices.append(left - 1)
    
    # Add weight to the bin
    self.values[tuple(indices)] += weight