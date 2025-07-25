def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale must be a numeric value")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        
    # Get the scaling factor
    factor = other / self._scale
    
    # Rescale the last coordinate and its errors
    if len(self.fields) > 0:
        last_field = self.fields[-1]
        
        # Scale the coordinate values
        self.data[last_field] *= factor
        
        # Scale any associated errors
        error_field = f"{last_field}_err"
        if error_field in self.data:
            self.data[error_field] *= factor
            
        sys_error_field = f"{last_field}_sys_err" 
        if sys_error_field in self.data:
            self.data[sys_error_field] *= factor
            
    # Update the scale
    self._scale = other
    
    return self