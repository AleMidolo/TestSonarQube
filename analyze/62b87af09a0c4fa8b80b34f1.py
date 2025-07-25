def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if self.is_within_bounds(coord):
        self.histogram[coord] += weight

def is_within_bounds(self, coord):
    """
    Check if the given coordinate is within the histogram bounds.
    """
    return all(0 <= c < dim for c, dim in zip(coord, self.histogram.shape))