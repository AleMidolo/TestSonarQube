def scale(self, other=None, recompute=False):
    # If scale is not computed yet or recompute is requested
    if self._scale is None or recompute:
        # Calculate integral of histogram
        self._scale = sum(self.values)
        
    # If other is None, return current scale
    if other is None:
        return self._scale
        
    # Cannot rescale if current scale is 0
    if self._scale == 0:
        raise LenaValueError("Cannot rescale histogram with zero scale")
        
    # Rescale histogram to other value
    if isinstance(other, (int, float)):
        scale_factor = other / self._scale
        self.values = [v * scale_factor for v in self.values]
        self._scale = other
    else:
        raise TypeError("Scale value must be a number")
        
    return self._scale