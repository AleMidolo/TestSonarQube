def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if not hasattr(self, 'errors'):
        raise AttributeError("The object does not have an 'errors' attribute.")
    
    if coord_name not in self.errors:
        raise KeyError(f"Coordinate '{coord_name}' not found in errors.")
    
    return self.errors[coord_name]