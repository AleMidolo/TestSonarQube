def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if not self.is_within_bounds(coord):
        return
    
    self.histogram[coord] += weight