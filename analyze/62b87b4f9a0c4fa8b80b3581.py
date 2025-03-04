def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale if already computed and no recompute requested
        if hasattr(self, '_scale') and not recompute:
            return self._scale
            
        # Calculate scale as integral of histogram
        self._scale = sum(self.data)
        return self._scale
        
    else:
        # Validate other is a float
        if not isinstance(other, (int, float)):
            raise TypeError("Scale value must be a number")
            
        # Get current scale
        current_scale = self.scale()
        
        # Check for zero scale
        if current_scale == 0:
            raise ValueError("Cannot rescale histogram with zero scale")
            
        # Calculate scale factor and apply to data
        scale_factor = other / current_scale
        self.data = [x * scale_factor for x in self.data]
        
        # Update stored scale
        self._scale = other
        
        return self