def scale(self, other=None, recompute=False):
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            # Calculate the scale (integral) of the histogram
            self._scale = sum(self.bins)
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("Scale factor must be a float or integer.")
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale.")
        # Rescale the histogram bins
        scale_factor = other / self._scale
        self.bins = [bin_value * scale_factor for bin_value in self.bins]
        self._scale = other