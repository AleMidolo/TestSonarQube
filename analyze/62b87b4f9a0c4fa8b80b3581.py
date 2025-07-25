def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale
        if self._scale is None or recompute:
            # Calculate scale as integral of histogram
            self._scale = sum(self.data)
        return self._scale
    else:
        # Rescale histogram to other
        current_scale = self.scale()
        
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Scale factor
        factor = float(other) / current_scale
        
        # Multiply all bins by scale factor
        self.data *= factor
        
        # Update scale
        self._scale = other
        
        return self