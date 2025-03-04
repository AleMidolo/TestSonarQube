def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale
        if self._scale is None or recompute:
            # Calculate scale as sum of bin contents
            self._scale = sum(self.bins)
        return self._scale
    else:
        # Rescale histogram to other
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Calculate scaling factor
        factor = float(other) / current_scale
        
        # Scale all bins
        self.bins = [bin_content * factor for bin_content in self.bins]
        
        # Update scale
        self._scale = other
        
        return self