def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale
        if self._scale is None or recompute:
            # Calculate scale if not computed or recompute requested
            self._scale = sum(self.data)
        return self._scale
    else:
        # Rescale histogram to other
        current_scale = self.scale()
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Calculate scaling factor and apply to data
        factor = float(other) / current_scale
        self.data = [x * factor for x in self.data]
        
        # Update scale
        self._scale = other
        return self