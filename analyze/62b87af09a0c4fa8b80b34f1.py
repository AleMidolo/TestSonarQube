def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if self.is_within_bounds(coord):
        self.histogram[coord] += weight