def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale must be a numeric value")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        
    # Get the last coordinate index
    last_coord_idx = len(self.coordinates) - 1
    if last_coord_idx < 0:
        return
        
    # Calculate scaling factor
    scale_factor = other / self._scale
    
    # Rescale the last coordinate values
    self.values[last_coord_idx] *= scale_factor
    
    # Rescale associated errors if they exist
    if hasattr(self, 'errors') and self.errors is not None:
        self.errors[last_coord_idx] *= scale_factor
        
    # Update the scale
    self._scale = other