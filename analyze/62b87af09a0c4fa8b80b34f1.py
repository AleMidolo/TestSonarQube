def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if not hasattr(self, 'histogram'):
        self.histogram = {}

    if coord in self.histogram:
        self.histogram[coord] += weight
    else:
        self.histogram[coord] = weight