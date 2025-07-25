def scale(self, other=None):
    if other is None:
        return self._scale
        
    if not isinstance(other, (int, float)):
        raise TypeError("Scale factor must be a number")
        
    if self._scale is None or self._scale == 0:
        raise LenaValueError("Cannot rescale chart with unknown or zero scale")
        
    # Get the last coordinate axis
    coords = self.get_coordinates()
    if not coords:
        return
        
    last_coord = coords[-1]
    scale_factor = other / self._scale
    
    # Rescale the last coordinate values
    self._data[last_coord] *= scale_factor
    
    # Rescale any associated errors
    error_name = f"{last_coord}_err"
    if error_name in self._data:
        self._data[error_name] *= scale_factor
        
    # Update the scale
    self._scale = other