def scale(self, other=None, recompute=False):
    # Return current scale if no other value provided
    if other is None:
        # Recompute scale if requested or not computed before
        if recompute or not hasattr(self, '_scale'):
            self._scale = sum(self.values())
        return self._scale
        
    # Set new scale
    else:
        # Convert other to float
        other = float(other)
        
        # Get current scale
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            from lena.core.exceptions import LenaValueError
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Calculate scaling factor and apply to all values
        factor = other / current_scale
        for key in self:
            self[key] *= factor
            
        # Update stored scale
        self._scale = other
        
        return self