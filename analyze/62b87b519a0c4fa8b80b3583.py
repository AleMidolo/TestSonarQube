def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale must be a numeric value")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        
    # Get the scale factor
    factor = other / self._scale
    
    # Get the last coordinate index
    last_coord = len(self.coordinates) - 1
    
    # Rescale the last coordinate and its errors
    self.coordinates[last_coord] *= factor
    
    if hasattr(self, 'errors') and self.errors is not None:
        for error in self.errors:
            if error[last_coord] is not None:
                error[last_coord] *= factor
                
    # Update the scale
    self._scale = other
    
    return self._scale