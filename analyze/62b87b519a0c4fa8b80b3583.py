def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale factor must be a number")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot scale a graph with unknown or zero scale")
        
    # Get the last coordinate field
    fields = self.fields()
    if not fields:
        raise LenaValueError("No fields found for scaling")
        
    last_coord = fields[-1]
    
    # Scale the last coordinate and its errors
    scale_factor = other / self._scale
    self._data[last_coord] *= scale_factor
    
    # Scale associated errors if present
    error_fields = [f for f in fields if f.startswith(f"{last_coord}_err")]
    for error_field in error_fields:
        self._data[error_field] *= scale_factor
        
    # Update the scale
    self._scale = other
    
    return self