def scale(self, other=None, recompute=False):
    """
    Compute or set scale (integral of the histogram).

    If *other* is ``None``, return scale of this histogram.
    If its scale was not computed before,
    it is computed and stored for subsequent use
    (unless explicitly asked to *recompute*).
    Note that after changing (filling) the histogram
    one must explicitly recompute the scale
    if it was computed before.

    If a float *other* is provided, rescale self to *other*.

    Histograms with scale equal to zero can't be rescaled.
    :exc:`.LenaValueError` is raised if one tries to do that.
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = sum(self.bins)
        return self._scale
    else:
        if not hasattr(self, '_scale') or recompute:
            self._scale = sum(self.bins)
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with scale equal to zero.")
        scale_factor = other / self._scale
        self.bins = [bin_value * scale_factor for bin_value in self.bins]
        self._scale = other