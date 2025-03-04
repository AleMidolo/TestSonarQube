def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale if already computed and recompute not requested
        if hasattr(self, '_scale') and not recompute:
            return self._scale
            
        # Calculate and store scale
        self._scale = sum(self.values())
        return self._scale
        
    else:
        # Get current scale
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Calculate scaling factor
        factor = float(other) / current_scale
        
        # Scale all values
        for key in self:
            self[key] *= factor
            
        # Update stored scale
        self._scale = other
        
        return self