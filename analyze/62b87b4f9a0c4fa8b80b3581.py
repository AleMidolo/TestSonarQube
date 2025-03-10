def scale(self, other=None, recompute=False):
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            # Calculate the scale (integral) of the histogram
            self._scale = sum(self.bin_values)  # Assuming bin_values is a list of bin values
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("Scale factor must be a float or integer.")
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale.")
        # Rescale the histogram
        self.bin_values = [value * other / self._scale for value in self.bin_values]
        self._scale = other