def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale if computed and not asked to recompute
        if hasattr(self, '_scale') and not recompute:
            return self._scale
            
        # Compute scale by integrating histogram
        scale = 0.0
        for bin_content in self.values():
            scale += bin_content
            
        # Store computed scale
        self._scale = scale
        return scale
        
    else:
        # Validate other is a float
        if not isinstance(other, (int, float)):
            raise TypeError("Scale must be a number")
            
        # Get current scale
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Compute scale factor
        factor = other / current_scale
        
        # Rescale all bins
        for key in self:
            self[key] *= factor
            
        # Update stored scale
        self._scale = other