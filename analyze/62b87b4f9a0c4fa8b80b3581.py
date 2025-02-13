def scale(self, other=None, recompute=False):
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = self._calculate_scale()
        return self._scale
    
    if isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale.")
        self._rescale(other)
    else:
        raise TypeError("Expected a float for 'other'.")