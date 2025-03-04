def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale if computed and not asked to recompute
        if hasattr(self, '_scale') and not recompute:
            return self._scale
            
        # Compute scale by integrating histogram
        self._scale = sum(self.values())
        return self._scale
        
    else:
        # Validate input
        if not isinstance(other, (int, float)):
            raise TypeError("Scale must be a number")
            
        # Get current scale
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Rescale histogram values
        scale_factor = other / current_scale
        for key in self:
            self[key] *= scale_factor
            
        # Update stored scale
        self._scale = other