def scale(self, other=None, recompute=False):
    if other is None:
        if not hasattr(self, '_scale_computed') or recompute:
            self._scale = sum(self.histogram)  # Assuming self.histogram is a list of histogram values
            self._scale_computed = True
        return self._scale
    else:
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with scale equal to zero.")
        scale_factor = other / self._scale
        self.histogram = [value * scale_factor for value in self.histogram]
        self._scale = other