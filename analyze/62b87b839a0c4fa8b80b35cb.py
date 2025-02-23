def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if coord_name not in self.data:
        raise ValueError(f"Coordinate '{coord_name}' not found in data.")
    
    error_indices = []
    for index, value in enumerate(self.data[coord_name]):
        if self.is_error(value):
            error_indices.append(index)
    
    return error_indices