def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale factor must be a number")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        
    # Get the last coordinate field
    fields = self.fields()
    if not fields:
        return
        
    last_coord = fields[-1]
    
    # Rescale the last coordinate values
    scale_factor = other / self._scale
    self._data[last_coord] *= scale_factor
    
    # Rescale any associated errors
    error_fields = [f for f in fields if f.startswith('error_')]
    for error_field in error_fields:
        if error_field.endswith(last_coord):
            self._data[error_field] *= scale_factor
            
    # Update the scale
    self._scale = other