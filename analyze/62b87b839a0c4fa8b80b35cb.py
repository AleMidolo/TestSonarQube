def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if not hasattr(self, 'error_indices'):
        raise AttributeError("The object does not have 'error_indices' attribute.")
    
    if coord_name not in self.error_indices:
        raise KeyError(f"Coordinate '{coord_name}' not found in error_indices.")
    
    return self.error_indices[coord_name]