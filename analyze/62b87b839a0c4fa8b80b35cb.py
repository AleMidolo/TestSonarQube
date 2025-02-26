def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if coord_name not in self.error_indices:
        raise ValueError(f"Coordinate name '{coord_name}' not found in error indices.")
    
    return self.error_indices[coord_name]