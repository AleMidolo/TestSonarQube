def scale(self, other=None, recompute=False):
    if other is None:
        # Return current scale if computed and not asked to recompute
        if hasattr(self, '_scale') and not recompute:
            return self._scale
            
        # Compute scale by integrating histogram
        scale = 0.0
        for bin_content in self.values():
            scale += bin_content
            
        # Store and return computed scale
        self._scale = scale
        return scale
        
    else:
        # Get current scale
        current_scale = self.scale()
        
        # Check if current scale is zero
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
            
        # Rescale histogram by multiplying all bins by ratio
        scale_ratio = float(other) / current_scale
        for bin in self:
            self[bin] *= scale_ratio
            
        # Update stored scale
        self._scale = float(other)