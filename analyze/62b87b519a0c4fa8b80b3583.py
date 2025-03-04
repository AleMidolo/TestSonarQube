def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale factor must be a number")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        
    # Get the scale factor
    factor = other / self._scale
    
    # Rescale the last coordinate and its errors
    if len(self.fields) > 0:
        last_field = self.fields[-1]
        
        # Rescale the coordinate values
        self.data[last_field] *= factor
        
        # Rescale any associated errors
        error_field = f"{last_field}_err"
        if error_field in self.data:
            self.data[error_field] *= factor
            
        # Rescale any asymmetric errors
        error_low = f"{last_field}_err_low"
        error_high = f"{last_field}_err_high"
        if error_low in self.data and error_high in self.data:
            self.data[error_low] *= factor
            self.data[error_high] *= factor
            
    # Update the scale
    self._scale = other
    
    return self